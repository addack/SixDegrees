# -*- coding: utf-8 -*-
'''
Created on Apr 30, 2011

@author: Michel Tricot
'''

from collections import defaultdict

class Stats(object):
    pass

class Graph(object):
    '''
    Graph is created using two maps. One contains the actors with all the 
    movies they were in. The second contain the distribution of all movies.
    This implementation reduces amount of data in memory that you would have 
    with adjacency list implementation. Drawback of this storage is that you
    need to recompute connections list at each request for it. 
    If you want to work fast on connections, use the getConnectionsBuckets.
    '''
    def __init__(self):
        self.movie_to_actor = defaultdict(list)
        self.actor_to_movie = defaultdict(list)
        
    
    def add(self, actor, movie):
        self.movie_to_actor[movie].append(actor)
        self.actor_to_movie[actor].append(movie)
       
    def getConnections(self, actor):
        '''
        Return set of all actor's connections. Connections are unique. 
        '''
        connections = set()
        for movie in self.actor_to_movie[actor]:
            connections.update(self.movie_to_actor[movie])
        return connections

    def getConnectionsBuckets(self, actor):
        '''
        Return list of all actor's connections for each movies. Connections
        are unique within the same bucket.
        You can use this function to avoid list copy.
        '''
        connections_buckets = []
        for movie in self.actor_to_movie[actor]:
            connections_buckets.append(self.movie_to_actor[movie])
        return connections_buckets

    def getInfo(self):
        '''
        Return some information about the graph.
        '''
        s = Stats()
        s.actors_count = len(self.actor_to_movie)
        s.movies_count = len(self.movie_to_actor)
        return s
        
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
