#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
Takes in the stdin file and parses for the transition and emission matrix
file should have input emission string as the first line
emissions on line 3, states on line 7 both are space delimited
matrix on line 10 and 11 tab delimited
'''
def hiddenPath(string, alphabet, transition, states, matrix):
    '''
    Input: string, emissions, states, transition matrix
    Output: probability of the emission based on the transition states
    '''
    d = {}
    matrix = matrix.astype(np.float)
    for i in range(len(alphabet)):
        d[alphabet[i]] = i
    for i in range(len(states)):
        d[states[i]] = i
    prob = matrix[d.get(transition[0]),d.get(string[0])]
    for i in range(1,len(string)):
        prob *= matrix[d.get(transition[i]),d.get(string[i])]
    return prob

def main():
    '''
    Input: file from stdin
    parses the file for the emission, state, and matrix data
    prints out the probability based on the path taken
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    alphabet = newLines[2].split()
    states = newLines[6].split()
    a = newLines[9].split('\t')
    b = newLines[10].split('\t')
    matrix = np.array([a[1:],b[1:]])
    print(hiddenPath(newLines[0],alphabet,newLines[4],states,matrix))

if __name__ == '__main__':
    main()
