#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes in from stdin a DAG in the form of an adjacency list
Outputs to stdout the eulerian path of in the graph 
computes in linear time
'''
class DirectedGraph:
    '''
    DAG class that take in the adjacency list to compute the eulerian path in linear time
    '''
    def __init__(self):
        '''
        initializes the outdegree and indegree dict and adjacency list
        '''
        self.degree = {}
        self.inDegree = {}
        self.adj = {}

    def insert(self,key,values):
        '''
        insert node into adjacency list
        '''
        self.adj[key] = values

    def outDegrees(self): 
        '''
        calculates all in and out degrees coming out for each node
        has to take multiple passes
        '''
        for key in self.adj:
            self.degree[key] = len(self.adj.get(key))
            self.inDegree[key] = 0 # get edge case nodes
        for key in self.adj:
            values = self.adj.get(key)
            for value in values:
                if value not in self.degree:
                    self.degree[value] = 0 # gets edge cases
                if value not in self.inDegree:
                    self.inDegree[value] = 1
                else:
                    self.inDegree[value] += 1
     

    def traverse(self):
        '''
        searches for a eulerian path in the graph in linear time
        assumes there is a eulerian path
        returns the path taken in an ordered list
        '''
        self.outDegrees()
        final = [] # final path
        visited = [] # current visited path
        key = self.start() # start node
        visited.append(key)
        current = self.adj.get(key)[self.degree.get(key)-1]
        self.degree[key] -= 1
        while current != None:
            visited.append(current)
            edge = self.degree.get(current) - 1 
            self.degree[current] -= 1 # removes edges to signify path used
            current = self.adj.get(current)[edge]
            if self.degree.get(current) == 0:
                current = self.backtrack(visited,final,current)
        return final[::-1] # fixes the reversal from using a stack

    def start(self):
        '''
        finds the start node that can find a eulerian path
        returns the start node based on the indegree and outdegree
        '''
        start = []
        for key in self.adj:
            if self.degree[key] == self.inDegree[key]+1: # this must be true if there is eulerian path
                start.append(key)
        if len(start) == 2: # there must be up to 2 startable nodes to be an eulers path
            if start[1] in self.adj.get(start[0]):
                return start[0]
            else:
                return start[1]
        else:
            return start[0]

    def backtrack(self,visited,final,current):
        '''
        backtracks to a node where there are unvisited nodes
        returns None if there aren't any
        '''
        while self.degree.get(current) == 0:
            final.append(current)
            if len(visited) == 0: # no more nodes to backtrack to
                return None
            current = visited.pop()
        return current

def main():
    '''
    takes in stdin of adjacency list and contstructs the DAG
    traverses the DAG to find a eulerian path and prints out to stdout
    '''
    lines = sys.stdin.readlines()
    graph = DirectedGraph()
    for value in lines:
        node = value.rstrip().split(' -> ')
        values = node[1].split(',')
        graph.insert(node[0],values)
    path = graph.traverse()
    current = path[0]
    for i in range(1,len(path)):
        current += '->' + path[i]
    print(current)

if __name__ == '__main__':
    main()
