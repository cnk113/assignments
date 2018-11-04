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
        truePath = False # Used when traversing graph and checks if this came from the start node
        if current in self.adj:
            self.adj.get(current).append(nextNode)
        else:
            self.adj[current] = [nextNode]
        if nextNode in self.weight:
            self.weight.get(nextNode).append((w,current,truePath))
        else:
            self.weight[nextNode] = [(w,current,truePath)]

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
        print(top)
        highestWeight = self.weight.copy()
        for node in top[top.index(start)+1:top.index(end)+1]:
            incoming = highestWeight.get(node)
            if incoming == None:
                continue
            highest = -1
            longest = incoming[0]
            for weights in incoming:
                if weights[1] == start:
                    weights = list(weights)
                    weights[2] = True
                    longest = tuple(weights)
                    outgoing = highestWeight.get(node)
                    for out in outgoing:
                        outWeights = list(out)
                        outWeights[2] = True
                        outWeights
                    break
                if highestWeight.get(weights[1]) == None:
                    continue
                print(weights)
                if highest < int(weights[0]):
                    if highestWeight.get(weights[1])[2] == True:
                        weights = list(weights)
                        weights[2] = True
                        longest = tuple(weights)
                    else:
                        highest = int(weights[0])
                        longest = weights
            if longest[2] == True:
                longest = list(longest)
                longest[0] += highestWeight.get(longest[1])[0]
                longest = tuple(longest)
                highestWeight[node] = longest
        current = end
        path = current
        while current != start:
            path = highestWeight.get(current)[1] + '->' + path
            current = highestWeight.get(current)[1]
        return (highestWeight.get(end)[0],path)
    
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
