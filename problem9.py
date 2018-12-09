#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes from stdin a file with a collections of kmers on every new line
Outputs to stdout the assembled sequence from the collection
'''

def assemble(seq):
    '''	
    assembles the entire sequence by appending the following string's last char
    returns the sequence
    '''
    sequence = seq[0]
    seq.pop(0)
    for s in seq:
        sequence += s[-1] # adds the last character of the string to the sequence
    return sequence

def main():
    '''
    takes in from stdin and removes the new lines after turning into a list
    prints out the the assembled string to stdout
    '''
    seq = sys.stdin.readlines()
    newSeq = []
    for s in seq:
       newSeq.append(s.rstrip())
    print(assemble(newSeq))

if __name__ == '__main__':
    main()
