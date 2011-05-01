# -*- coding: utf-8 -*-
'''
Created on May 1, 2011

@author: Addack
'''

import logging
import time

class LayerGenerator(object):
    
    def __init__(self, graph, actor):
        self.graph = graph
        self.actor = actor
        
    def __iter__(self):
        current_layer = set([self.actor])
        old_layers = set()
        while current_layer:
            yield current_layer
            t = time.time()
            new_layer = set()
            for actor in current_layer:
                connections_buckets = self.graph.get_connections_buckets(actor)
                for connections_bucket in connections_buckets:
                    new_layer.update(connections_bucket)
            old_layers |= current_layer
            new_layer -= old_layers
            current_layer = new_layer
            logging.info('Exploration layer #: %s, built in %s' % 
                         (len(current_layer), time.time() - t))
