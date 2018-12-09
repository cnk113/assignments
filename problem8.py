#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes in from stdin a file with size of kmer on first line
And the sequence string on the second line
Outputs to stdout
'''

def composition(k,seq):
    '''
    returns the kmer composition at size k
    uses a sliding window of size k
    '''
    lis = []
    for i in range(len(seq)-int(k)+1):
        lis.append(seq[i:i+int(k)])
    return sorted(lis)

def main():
    '''
    reads in kmer size from stdin and strips newlines
    outputs composition to stdout
    '''
    lines = sys.stdin.readlines()
    comp = composition(lines[0].rstrip(),lines[1].rstrip())
    for s in comp:
        print(s)

if __name__ == '__main__':
    main()
