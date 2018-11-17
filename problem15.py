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
        self.degree = {}

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
     
    def topologicalSort(self):
        '''
        topological sorting using khans algorithm, uses degrees instead of edge destruction
        '''
        for key in self.adj:
            self.degree[key] = 0
        for key in self.incoming:
            self.degree[key] = 0
        for key in self.incoming:
            self.degree[key] += len(self.incoming.get(key))
        copied = self.degree.copy()
        top = []
        stack = []
        for node in self.degree:
            if copied.get(node) == 0:
                stack.append(node)
        while len(stack) != 0:
            current = stack.pop()
            top.append(current)
            nodes = self.adj.get(current)
            if nodes == None:
                continue
            for node in nodes:
                copied[node] -= 1
                if copied.get(node) == 0:
                    stack.append(node)
        return top

    def longestPath(self,top,start,end):
        '''
        scores the highest incoming weight of each node
        returns the path from the end node to start node
        '''
        score = {}
        source = {}
        for node in top:
            if node == start:
                score[node] = 0
            elif self.degree.get(node) == 0 and node != start:
                score[node] = -inf
            else:
                incoming = self.incoming.get(node)
                highest = incoming[0]
                for nodes in incoming:
                    if score.get(highest[1]) + int(highest[0]) < score.get(nodes[1]) + int(nodes[0]):
                        highest = nodes
                score[node] = int(highest[0]) + score.get(highest[1])
                source[node] = highest[1]
        current = end
        path = current
        while current != start:
            path = source.get(current) + '->' + path
            current = source.get(current)
        return (score.get(end),path)
        
    
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
    path = dag.longestPath(dag.topologicalSort(),new[0],new[1])
    print(path[0])
    print(path[1])

if __name__ == "__main__":
    main()
