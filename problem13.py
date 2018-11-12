#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
'''
class DirectedGraph:
    '''
    '''
    def __init__(self):
        '''
        '''
        self.degree = {}
        self.adj = {}
        self.length = 0

    def insert(self,key,values):
        '''
        '''
        self.adj[key] = values

    def outDegrees(self): 
        '''
        '''
        for key in adj:
            values = self.adj.get(key)
            if key in self.degree:
                self.degree[key] += len(values)
            else:
                self.degree[key] = len(values)

    def traverse(self):
        '''
        '''
        final = []
        visited = []
        for key in self.adj:
            visited.append(key)
            current = self.adj.get(key)[self.degree.get(key)-1]
            self.degree[key] -= 1
            break
        while current != None:
            visited.append(current)
            edge = self.degree.get(current) - 1
            self.degree[current] -= 1
            current = self.adj.get(current)[edge]
            if self.degree.get(current) == 0:
                current = self.backtrack(visited,final,current)
        return final

    def backtrack(self,visited,final,current):
        '''
        '''
        final.append(current)
        while self.degree.get(current) == 0:
            if len(visited) == 0:
                return None
            current = visited.pop()
            final.append(current)
        visited.append(final.pop())
        return current

def main():
    '''
    '''
    lis = sys.stdin.readlines()
    graph = DirectedGraph()
    for value in lis:
        node = value.rstrip().split(' -> ')
        values = node[1].split(',')
        graph.insert(node[0],values)
    graph.outDegrees()
    path = graph.traverse()
    current = path[0]
    for i in range(1,len(path)):
        current.append('->' + path[i])
    print(current)

if __name__ == '__main__':
	main()
