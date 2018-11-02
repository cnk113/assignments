#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

def construct(lis):
    k = int(lis[0])
    kmers = lis[1:]
    string = kmers[0]
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        kmers.remove(kmer)
        for other in kmers:
    	    otherPrefix = other[:-1]
    	    otherSuffix = other[1:]
    	    if suffix == otherPrefix:
                string += other[k-1]
    	    elif prefix == otherSuffix:
    	        string = kmer[0] + string
    return string

def main():
    lis = sys.stdin.readlines()
    new = []
    for s in lis:
        new.append(s.rstrip())
    print(construct(new))

if __name__ == '__main__':
	main()