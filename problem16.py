#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
Input: Takes in a file through stdin
Output: probability of the path based on transtion matrix
initial probability is agnostic
format of the file should have a string as the first line
line 3 for the states, space delimited
line 6,7 for the transition matrix, tab delmited
'''
def hiddenPath(string,states,matrix):
    '''
    calculates the probability of the string based on the transition matrix
    '''
    d = {}
    matrix = matrix.astype(np.float)
    for i in range(len(states)):
        d[states[i]] = i
    prob = .5
    for i in range(1,len(string)):
        prob *= matrix[d[string[i-1]],d[string[i]]]
    return prob

def main():
    '''
    takes in the input and parses for the string and transition matrix
    prints out the probability from the hiddenPath function
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    states = newLines[2].split()
    a = newLines[5].split('\t')
    b = newLines[6].split('\t')
    matrix = np.array([a[1:],b[1:]])
    print(hiddenPath(newLines[0],states,matrix))

if __name__ == '__main__':
    main()
