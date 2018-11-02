#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

def composition(opts):
    '''
    returns the kmer composition
    '''
    k = int(opts[0])
    seq = opts[1]
    lis = []
    for i in range(len(seq)-k+1):
        lis.append(seq[i:i+k])
    return sorted(lis)

def main():
    '''
    reads in kmer size and string and outputs composition
    '''
    opts = sys.stdin.readlines()
    comp = composition(opts)
    for s in comp:
        print(s)

if __name__ == '__main__':
    main()
