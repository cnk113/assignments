#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

def deBrujin(lis):
    '''
    creates a debrujin adjacency list form from the string
    '''
    k = int(lis[0])-1
    seq = lis[1]
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
    
    '''
    lis = sys.stdin.readlines()
    adj = deBrujin(lis)
    for key in adj:
        print(key + " -> " + adj.get(key))

if __name__ == '__main__':
    main()