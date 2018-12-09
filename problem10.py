#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes input from stdin of a collections of kmers seperated by newlines
Outputs the overlap graph in an adjacency list through stdout
'''
def adjacencyList(string):
    '''
    constructs the adjacency list from the prefix of one sequence and
    suffix of another sequence in the collection
    returns adjacency list
    '''
    adj = {}
    for seq in string:
        suffix = seq[1:]
        for others in string:
            prefix = others[:-1]
            if prefix == suffix:
                adj[seq] = others
    return adj

def main():
    '''
    strips newlines from the stdin list
    prints out the adjacency list to stdout
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for seq in lines:
        newLines.append(seq.rstrip())
    adj = adjacencyList(newLines)
    for key in adj:
    	print(key + " -> " + adj.get(key))

if __name__ == '__main__':
    main()
