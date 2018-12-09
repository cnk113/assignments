#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes in from stdin and a string of sequences
Outputs to stdout the deBrujin graph as an adjacency list
'''

def deBrujin(k,seq):
    '''
    creates a debrujin adjacency list form from the string
    nodes k-1 long and kth sequence is the edge
    returns adjacency list
    '''
    k = int(k)-1
    adj = {}
    for i in range(len(seq)-k):
        first = seq[i:i+k]
        second = seq[i+1:i+k+1]
        if first in adj:
            adj[first] = adj.get(first) + ',' + second
        else:
            adj[first] = second
    return adj

def main():
    '''
    reads in fron stdin and strips the lines of newlines
    runs the deBrujin function and prints out the adjacency lsit
    '''
    lines = sys.stdin.readlines()
    adj = deBrujin(lines[0].rstrip(),lines[1].rstrip())
    for key in adj:
        print(key + " -> " + adj.get(key))

if __name__ == '__main__':
    main()
