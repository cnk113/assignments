#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

class Graph:
    def __init__(self,start,end,lis):
    	self.start = start
    	self.end = end
        self.adj = {}
        for nodes in lis:
            node = nodes.split(' -> ')
            values = node[1].split(':')
            if values[0] in self.adj[node[0]]:
                self.adj[node[0]] = self.adj.get(node[0]).append(values[0])
            else:
                self.adj[node[0]] = [values[0]]

    def topologicalSort(self):
    	degree = {}
    	for key in self.adj:
    	    degree[key] = 0
        for key in self.adj:
            nodes = self.adj.get(key)
            for node in nodes:
                degree[node] += 1
        top = []
        stack = []
        for node in degree:
            if degree.get(node) == 0:
                stack.append(node)
        while len(stack) != 0:
            current = stack.pop()
            self.top.append(current)
            nodes = self.adj.get(current)
            for node in nodes:
                degree[node] -= 1
                if degree.get(node) = 0:
                    stack.append(node)
        return top

    def calculateWeights(self,top):
        for node in top:



def main():
    lis = sys.stdin.readlines().strip()
    graph = Graph(lis[0],lis[1],lis[2:])
    graph.calculateWeights(graph.topologicalSort())


if __name__ == "__main__":
    main()
