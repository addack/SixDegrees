# -*- coding: utf-8 -*-
'''
Created on May 2, 2011

@author: Michel Tricot
'''

import cmd
import logging
import re
import sys
import time

import degree_finder
import graph

def timed_function(f):
    def time_function_internal(self, line):
        t = time.time()
        f(self, line)
        #logging.INFO('Total computation took: %s' % (time.time() - t))
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
        '''
        s = self.graph.get_info()
        print('#actors: %s, #movies: %s' % (s.actors_count, s.movies_count))

    def do_set(self, line):
        '''
        Sets starting actor.
        '''
        self.actor = line.strip()

    def do_current(self, line):
        '''
        Prints currently set actor.
        '''
        print(self.actor)

    #@timed_function
    def do_degree(self, line):
        '''
        Computes degree between currently set actor and provided destination actor. 
        '''
        print(self.degree.compute_degree(self.actor, line))
    
    #@timed_function
    def do_max_degree(self, line):
        '''
        Computes last available layer and degree for currently set actor.
        '''
        print(self.degree.compute_max_degree(self.actor))
    
    def do_search(self, line):
        '''
        Searches all actors matching provided regexp.
        '''
        searcher = re.compile(line)
        for name in self.graph.actor_to_movie:
            if searcher.search(name):
                print name
    
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
