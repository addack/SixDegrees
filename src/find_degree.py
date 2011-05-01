# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2011

@author: Michel Tricot
'''

import sys
import graph
import layer_generator
import time

def find_degree_old(g, from_actor, to_actor):
    degree = 0
    current_layer = set([from_actor])
    old_layers = set()
    while not to_actor in current_layer:
        t = time.time()
        degree += 1
        print 'Investigating degree %s' % degree
        new_layer = set()
        for actor in current_layer:
            connections_buckets = g.getConnectionsBuckets(actor)
            for connections_bucket in connections_buckets:
                new_layer.update(connections_bucket)
        old_layers |= current_layer
        new_layer -= old_layers
        current_layer = new_layer
        print("exploration layer #: %s, built in %s" % (len(current_layer),
                                                        time.time() - t))
    return degree

def find_degree(g, from_actor, to_actor):
    layers = layer_generator.LayerGenerator(g, from_actor)
    degree = 0
    for layer in layers:
        if to_actor in layer:
            print degree
            break
        degree += 1

def find_max_degree(g, from_actor):
    layers = layer_generator.LayerGenerator(g, from_actor)
    degree = 0
    old_layer = None
    for layer in layers:
        if not layer:
            break
        old_layer = layer
        degree += 1
    print old_layer
    

def main():
    g = graph.load_graph(sys.argv[1])
    print "load complete"
    print(g.displayStat())
    #print find_degree(g, 'Pitt, Brad', 'Reno, Jean (I)')
    print find_max_degree(g, 'Pitt, Brad')
    #print find_degree(g, 'Pitt, Brad', 'Hong, Duyen')
    #print find_degree(g, 'Pitt, Brad', 'Klooren, Mati')
    

if __name__ == '__main__':
    main()