#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

def pairwise(l):
    '''
    pairwise comparison of the prefix and suffix
    '''
    adj = {}
    for seq in l:
        suffix = seq[1:]
        for others in l:
            prefix = others[:-1]
            if prefix == suffix:
                adj[seq] = others
    return adj

def main():
    '''
    strips newlines from the list
    prints out the graph
    '''
    l = sys.stdin.readlines()
    new = []
    for seq in l:
        new.append(seq.rstrip())
    adj = pairwise(new)
    for key in adj:
    	print(key + " -> " + adj.get(key))

if __name__ == '__main__':
	main()