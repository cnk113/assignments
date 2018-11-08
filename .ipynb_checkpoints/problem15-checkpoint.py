#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
from math import inf

'''
Finds longest path from a start node to the end 
assuming no cycle in between the start and end node
'''
class DirectedAcyclicGraph: 
    '''
    DAG object
    '''
    def __init__(self):
        '''
        graph has three dicts: one for adjacent nodes, 
        one for incoming nodes (includes weights), and last for the overall score (highest weight from incoming)
        '''
        self.adj = {}
        self.incoming = {}
        self.score = {}

    def insert(self,nodes):
        '''
        inserts the node into the graph and the dictionaries
        '''
        node = nodes.split('->')
        values = node[1].split(':')
        current = node[0]
        nextNode = values[0]
        w = values[1]
        if current in self.adj:
            self.adj.get(current).append(nextNode)
        else:
            self.adj[current] = [nextNode]
        if nextNode in self.incoming:
            self.incoming.get(nextNode).append([w,current])
        else:
            self.incoming[nextNode] = [[w,current]]
     
    def topologicalSort(self,start):
        '''
        topological sorting using khans algorithm, uses degrees instead of edge destruction
        '''
        degree = {}
        for key in self.adj:
            degree[key] = 0
        for key in self.adj:
            nodes = self.adj.get(key)
            for node in nodes:
                if node not in degree:
                    degree[node] = 1
                else:
                    degree[node] += 1
        top = []
        stack = []
        for node in degree:
            if degree.get(node) == 0:
                stack.append(node)
                if node != start:
                    self.score[node] = -inf # Sets the score of the start nodes at -inf
                else:
                    self.score[node] = 0 # Only the start node is set to 0
        removal = stack.copy()
        while len(stack) != 0:
            current = stack.pop()
            top.append(current)
            nodes = self.adj.get(current)
            if nodes == None:
                continue
            for node in nodes:
                degree[node] -= 1
                if degree.get(node) == 0:
                    stack.append(node)
        for node in removal: # Removes all start nodes since they already have a score
            top.remove(node)
        return top

    def longestPath(self,top,start,end):
        '''
        scores the highest incoming weight of each node
        returns the path from the end node to start node
        '''
        for node in top:
            incoming = self.incoming.get(node)
            highest = incoming[0]
            for nodes in incoming:
                if self.score.get(highest[1]) < self.score.get(nodes[1]):
                    highest = nodes
            self.score[node] = int(highest[0]) + self.score.get(highest[1])
            self.incoming[node] = highest
        current = end
        path = current
        while current != start:
            path = self.incoming.get(current)[1] + '->' + path
            current = self.incoming.get(current)[1]
        return (self.score.get(end),path)
        
    
def main():
    '''
    creates graph and inputs the nodes into the graph
    '''
    lis = sys.stdin.readlines()
    new = []
    for s in lis:
        new.append(s.rstrip())
    dag = DirectedAcyclicGraph()
    for node in new[2:]:
        dag.insert(node)
    path = dag.longestPath(dag.topologicalSort(new[0]),new[0],new[1])
    print(path[0])
    print(path[1])

if __name__ == "__main__":
    main()
