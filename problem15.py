#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
'''
class DirectedAcyclicGraph: 
    '''
    '''
    def __init__(self):
        '''
        '''
        self.adj = {}
        self.weight = {}

    def insert(self,nodes):
        '''
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
        if nextNode in self.weight:
            self.weight.get(nextNode).append((w,current))
        else:
            self.weight[nextNode] = [(w,current)]

    def topologicalSort(self):
        '''
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
        return top

    def longestPath(self,top,start,end):
        '''
        '''
        highestWeight = {}
        front = top.index(start)
        back = top.index(end)
        for i in range(front,back+1):
            incoming = self.weight.get(top[i])
            if incoming == None:
                continue
            highest = -1
            for weights in incoming:
                if weights[1] == start:
                    longest = weights
                    break
                elif highest < int(weights[0]):
                    longest = weights
                    highest = int(weights[0])
            highestWeight[top[i]] = longest
        current = end
        path = current
        weight = 0
        while current != start:
            path = highestWeight.get(current)[1] + '->' + path
            weight += int(highestWeight.get(current)[0])
            current = highestWeight.get(current)[1]
        return (weight,path)

def main():
    '''
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
