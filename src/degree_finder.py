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
        '''
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
