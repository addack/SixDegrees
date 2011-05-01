# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2011

@author: Michel Tricot
'''

import logging
import sys

import graph
import layer_generator

def find_degree(g, from_actor, to_actor):
    layers = layer_generator.LayerGenerator(g, from_actor)
    degree = 0
    for layer in layers:
        if to_actor in layer:
            break
        degree += 1
    return degree

def find_max_degree(g, from_actor):
    layers = layer_generator.LayerGenerator(g, from_actor)
    old_layer = None
    for layer in layers:
        old_layer = layer
    print old_layer

def main():
    logging.basicConfig(level=logging.INFO)
    g = graph.load_graph(sys.argv[1])
    s = g.getInfo()
    logging.info('#actors: %s, #movies: %s' % (s.actors_count, s.movies_count))
    
    #print find_degree(g, 'Pitt, Brad', 'Reno, Jean (I)')
    print find_max_degree(g, 'Pitt, Brad')
    #print find_degree(g, 'Pitt, Brad', 'Hong, Duyen')
    #print find_degree(g, 'Pitt, Brad', 'Klooren, Mati')
    

if __name__ == '__main__':
    main()
