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

def expect_argument(error):
    def expect_argument_wrap(f):
        @functools.wraps(f)
        def expect_argument_internal(*args, **kwargs):
            t = time.time()
            if len(args) == 2 and args[1]:
                f(*args, **kwargs)
            else:
                print error
        return expect_argument_internal
    return expect_argument_wrap


class SixDegreesCmd(cmd.Cmd):
    
    def __init__(self, g):
        cmd.Cmd.__init__(self)
        self.prompt = '6d> '
        self.intro = "SixDegree example"
        self.actor = None
        self.graph = g
        self.degree = degree_finder.DegreeFinder(g)

    def validate_actor(self, actor):
        return actor in self.graph.actor_to_movie

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

    @expect_argument('Please provide source actor to use')
    def do_set(self, line):
        '''
        Sets starting actor.
        Eg:
        6d> set Clooney, George
        '''
        self.actor = line.strip()
        if not self.validate_actor(self.actor):
            self.actor = None
        print self.actor

    def do_current(self, line):
        '''
        Prints currently set actor.
        6d> set Clooney, George
        6d> current
        Clooney, George 
        '''
        print(self.actor)

    @expect_argument('Please provide destination actor')
    @timed_log
    def do_degree(self, line):
        '''
        Computes degree between currently set actor and provided destination actor.
        Eg:
        6d> set Clooney, George
        6d> degree Klooren, Mati
        3 
        '''
        if self.validate_actor(self.actor) and self.validate_actor(line):
            print('Found at degree %s' % self.degree.compute_degree(self.actor, line))
        else:
            print('Please provide valid input and output actors')
    
    @timed_log
    def do_max_degree(self, line):
        '''
        Computes last available layer and degree for currently set actor.
        Eg:
        6d> set Clooney, George
        6d> max_degree
        (8, set(['Hong, Duyen', 'Phuc, Henry', 'Thu, Hang', 'Hong, Phuong']))
        '''
        if self.validate_actor(self.actor):
            print('Last layer is %s' % self.degree.compute_max_degree(self.actor))
        else:
            print('Please provide valid input actor')

    @expect_argument('Please provide regexp of an actor name to search for')    
    def do_search(self, line):
        '''
        Searches all actors matching provided regexp.
        Eg:
        6d> search Clooney.*
        Clooney, Andrew
        Clooney, Nick
        Clooney, George
        '''
        try:
            searcher = re.compile(line)
            for name in self.graph.actor_to_movie:
                if searcher.search(name):
                    print name
        except Exception, e:
            print(e)
    
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
