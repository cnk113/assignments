#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes in from stdin and a collection of kmers seperated by new lines
Outputs to stdout the adjacency of a deBrujin graph
'''

def deBrujin(lines):
    '''
    constructs the deBrujin graph in the form of an adjacency
    creates the list by the prefix -> suffix of the kmers
    the node is k-1 and kth value as the edge
    returns the adjacency list
    '''
    adj = {}
    for seq in lines:
        prefix = seq[:-1]
        suffix = seq[1:]
        if prefix in adj: # if already exists
            adj[prefix] = adj.get(prefix) + ',' + suffix
        else:
            adj[prefix] = suffix
    return adj

def main():
    '''
    strips lines fron stdin from newlines
    runs the deBrujin function to get the adjacency list
    prints out the adjacency list to stdout
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for seq in lines:
       newLines.append(seq.rstrip())
    adj = deBrujin(newLines)
    for key in adj:
        print(key + " -> " + adj.get(key))

if __name__ == '__main__':
    main()
