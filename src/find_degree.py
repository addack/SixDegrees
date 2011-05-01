# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2011

@author: Addack
'''

import logging
import sys

import graph
import degree_finder

def main():
    g = graph.load_graph(sys.argv[1])
    s = g.get_info()
    logging.info('#actors: %s, #movies: %s' % (s.actors_count, s.movies_count))

    degree = degree_finder.DegreeFinder(g)    
    #print degree.compute_max_degree('Pitt, Brad')
    print degree.compute_degree('Pitt, Brad', 'Hong, Duyen')
    #print degree.compute_degree('Pitt, Brad', 'Klooren, Mati')
    #print degree.compute_degree('Pitt, Brad', 'Reno, Jean (I)')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
