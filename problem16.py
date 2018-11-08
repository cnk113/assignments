#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

def hiddenPath(string,states,matrix):
    '''
    calculates the probability of the string based on the transition matrix
    '''
    if string[0] == states[0]:
        prev = 0
    else:
        prev = 1
    prob = 
    for i in range(1,len(string)):
        if string[i] == states[0]:
             prob *= matrix[prev,0]
             prev = 0
        else:
             prob *= matrix[prev,1]
             prev = 1
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
