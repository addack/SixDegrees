# -*- coding: utf-8 -*-
'''
Created on May 1, 2011

@author: Addack
'''

import layer_generator

class DegreeFinder(object):
    '''
    Provide methods to extract degree information.
    '''    

    def __init__(self, graph):
        self.graph = graph
        
    def compute_degree(self, from_actor, to_actor):
        '''
        Returns degree between two actors.
        Small optimization when providing input, we start with the actor with the 
        less connections so it can result in smaller layer.
        '''
        first_bucket = self.graph.get_connections_buckets(from_actor)
        second_bucket = self.graph.get_connections_buckets(to_actor)
        if len(first_bucket) > len(second_bucket):
            to_actor, from_actor = from_actor, to_actor
        layers = layer_generator.LayerGenerator(self.graph, from_actor)
        degree = 0
        for layer in layers:
            if to_actor in layer:
                break
            degree += 1
        return degree
    
    def compute_max_degree(self, actor):
        '''
        Returns actor's last layer and degree.
        '''
        layers = layer_generator.LayerGenerator(self.graph, actor)
        old_layer = None
        degree = -1
        for layer in layers:
            old_layer = layer
            degree += 1
        return degree, old_layer
