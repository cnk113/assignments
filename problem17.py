#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

def hiddenPath(string, alphabet, transition, states, matrix):
    d = {'x':0,'y':1,'z':2,'A':0,'B':1}
    for i in range(len(alphabet)):
        d[alphabet[i]] = i
    for i in range(len(states)):
        d[states[i]] = i
    prob = matrix[d.get(transition[0]),d.get(string[0])]
    for i in range(1,len(string)):
        prob *= matrix[d.get(transition[i]),d.get(string[i])]
    return prob

def main():
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(lines.rstrip())
    alphabet = newLines[2].split()
    states = newLines[6].split()
    a = newLines[9].split('\t')
    b = newLines[10].split('\t')
    matrix = np.array(a[1:],b[1:])
    print('{.11e}'.format(hiddenPath(newLines[0],alphabet,newLines[4],states,matrix)))

if __name__ == '__main__':
    main()
