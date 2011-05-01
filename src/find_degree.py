# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2011

@author: Michel Tricot
'''

import logging
import sys

import graph
import degree_finder

def main():
    g = graph.load_graph(sys.argv[1])
    s = g.getInfo()
    logging.info('#actors: %s, #movies: %s' % (s.actors_count, s.movies_count))

    degree = degree_finder.DegreeFinder(g)    
    print degree.computeMaxDegree('Pitt, Brad')
    print degree.computeDegree('Pitt, Brad', 'Hong, Duyen')
    print degree.computeDegree('Pitt, Brad', 'Klooren, Mati')
    print degree.computeDegree('Pitt, Brad', 'Reno, Jean (I)')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
