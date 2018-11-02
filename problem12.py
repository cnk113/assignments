#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

def deBrujin(lis):
    adj = {}
    k = len(lis[0])-1
    for seq in lis:
        prefix = seq[:-1]
        suffix = seq[1:]
        if prefix in adj:
            adj[prefix] = adj.get(prefix) + ',' + suffix
        else:
            adj[prefix] = suffix
    return adj

def main():
    lis = sys.stdin.readlines()
    new = []
    for s in lis:
       new.append(s.rstrip())
    adj = deBrujin(new)
    for key in adj:
        print(key + " -> " + adj.get(key))

if __name__ == '__main__':
	main()