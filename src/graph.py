# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2011

@author: Michel Tricot
'''

from collections import defaultdict

class Graph(object):
    
    def __init__(self):
        #self.nodes = defaultdict(lambda: defaultdict(set))
        self.movie_to_actor = defaultdict(list)
        self.actor_to_movie = defaultdict(list)
        
    
    def add(self, actor, movie):
        self.movie_to_actor[movie].append(actor)
        self.actor_to_movie[actor].append(movie)
       
    def getConnections(self, actor):
        connections = []
        for movie in self.actor_to_movie[actor]:
            connections.extend(self.movie_to_actor[movie])
        return connections

    def getConnectionsBuckets(self, actor):
        connections_buckets = []
        for movie in self.actor_to_movie[actor]:
            connections_buckets.append(self.movie_to_actor[movie])
        return connections_buckets

    def displayStat(self):
        print('#actor: %s #movie: %s' % (len(self.actor_to_movie), 
                                         len(self.movie_to_actor)))

def load_graph(file):
    graph = Graph()
    
    with open(file) as f:
        current_movie = None

        for line in f:
            if line[0] != '\t':
                current_movie = line.strip()
            else:
                graph.add(line.strip(), current_movie)
    
    return graph
