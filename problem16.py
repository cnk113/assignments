#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

def hiddenPath(string,states,matrix):
    '''
    calculates the probability of the string based on the transition matrix
    '''
    d = {}
    for i in range(len(states)):
        d[states[i]] = i
    prob = matrix[d.get(string[0]),d.get(string[1])]
    for i in range(2,len(string)):
        prob *= matrix[d.get(string[i-1],d.get(string[i]))
    return prob

def main():
    '''
    takes in the input and parses for the string and transition matrix
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(lines.rstrip())
    states = newLines[2].split()
    a = newLines[5].split('\t')
    b = newLines[6].split('\t')
    matrix = np.array(a[1:],b[1:])
    print('{:11e}'.format(hiddenPath(newLines[0],states,matrix)))

if __name__ == '__main__':
    main()
