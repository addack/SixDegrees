# -*- coding: utf-8 -*-
'''
Created on May 2, 2011

@author: Michel Tricot
'''

import cmd
import functools
import logging
import re
import sys
import time

import degree_finder
import graph

def timed_log(f):
    @functools.wraps(f)
    def time_function_internal(*args, **kwargs):
        t = time.time()
        f(*args, **kwargs)
        logging.info('Total computation took: %s' % (time.time() - t))
    return time_function_internal

class SixDegreesCmd(cmd.Cmd):
    
    def __init__(self, g):
        cmd.Cmd.__init__(self)
        self.prompt = '6d> '
        self.intro = "SixDegree example"
        self.actor = None
        self.graph = g
        self.degree = degree_finder.DegreeFinder(g)

    def do_enable_log(self, line):
        '''
        Enables logging, display calculation information...
        '''
        logging.getLogger().setLevel(logging.INFO)
        
    def do_disable_log(self, line):
        '''
        Disables logging.
        '''
        logging.disable(logging.INFO)
    
    def do_show_stats(self, line):
        '''
        Shows some graph's information.
        Eg:
        6d> show_stats
        #actors: 1327007, #movies: 604208
        '''
        s = self.graph.get_info()
        print('#actors: %s, #movies: %s' % (s.actors_count, s.movies_count))

    def do_set(self, line):
        '''
        Sets starting actor.
        Eg:
        6d> set Clooney, George
        '''
        self.actor = line.strip()

    def do_current(self, line):
        '''
        Prints currently set actor.
        6d> set Clooney, George
        6d> current
        Clooney, George 
        '''
        print(self.actor)

    @timed_log
    def do_degree(self, line):
        '''
        Computes degree between currently set actor and provided destination actor.
        Eg:
        6d> set Clooney, George
        6d> degree Klooren, Mati
        3 
        '''
        print(self.degree.compute_degree(self.actor, line))
    
    @timed_log
    def do_max_degree(self, line):
        '''
        Computes last available layer and degree for currently set actor.
        Eg:
        6d> set Clooney, George
        6d> max_degree
        (8, set(['Hong, Duyen', 'Phuc, Henry', 'Thu, Hang', 'Hong, Phuong']))
        '''
        print(self.degree.compute_max_degree(self.actor))
    
    def do_search(self, line):
        '''
        Searches all actors matching provided regexp.
        Eg:
        6d> search Clooney.*
        Clooney, Andrew
        Clooney, Nick
        Clooney, George
        '''
        searcher = re.compile(line)
        for name in self.graph.actor_to_movie:
            if searcher.search(name):
                print name
    
    def do_quit(self, line):
        '''
        Exits program.
        '''
        return True
    
    def do_EOF(self, line):
        return True
    
    def emptyline(self):
        pass


def main():
    g = graph.load_graph(sys.argv[1])
    interpretor = SixDegreesCmd(g)
    interpretor.cmdloop()
    
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    main()
