#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys


class Graph:
    def __init__():
        self.adj = {}
        total = 0
        for nodes in lis:
            node = nodes.split(' -> ')
            values = node[1].split(',')
            adj[node[0]] = values
        total += len(values)

    def getNode():

    def 

def findPath(tup):
    adj = tup[0]
    total = tup[1]
    keys = list(adj.keys())
    for start in keys:
        current = start
        visited = traverse(adj,total,current,keys)
        if len(visited) == total:
            return visited

def traverse(adj,total,current,keys):
    unused = []
    visited = [current]
    restart = False
    while restart == False: # traversal
        print(visited)
        current = getNext(adj,current)
        if current == None:
            restart = backtrack(adj,current,visited,unused,keys)
        else:
            visited.append(current) # adds to visited
            if getUnunsed(adj,current) == None:
                pass    
            elif len(getUnunsed(adj,current)) > 0:
                unused.append((current,getUnunsed(adj,current))) # stores the current node and nodes that are unused in a tuple
    return visited

def backtrack(adj,current,visited,unused,keys):
    if len(unused) == 0: # if there is no more unused edges, a dead end
        return True
    new = unused[len(unused)-1] # gets last ununsed edge
    visited = visited[:visited.index(new[0])+1] # backtracks
    current = new[1].pop(0) # removes the unused node after being used
    visited.append(current)
    if getUnunsed(adj,current) == None:
        pass    
    elif len(getUnunsed(adj,current)) > 0:
        unused.append((current,getUnunsed(adj,current)))
    if len(new[1]) == 0:
        unused.pop() # removes the entire node and edges if there are no more unused edges
    return False

def getNext(adj,node):
    nodes = adj.get(node)
    if nodes == None:
        return None
    return nodes[0]

def getUnunsed(adj,node):
    nodes = adj.get(node)
    if nodes == None:
        return None
    return nodes[1:]  

def constructAdjacencyList(lis):
    adj = {}
    total = 0
    for nodes in lis:
        node = nodes.split(' -> ')
        values = node[1].split(',')
        adj[node[0]] = values
        total += len(values)
    return (adj,total)

def main():
    lis = sys.stdin.readlines()
    new = []
    for s in lis:
       new.append(s.rstrip())
    path = findPath(constructAdjacencyList(new))
    p = path[0]
    path.remove(p)
    for node in path:
        p += '->' + node
    print(p)

if __name__ == '__main__':
	main()
