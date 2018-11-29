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
line 6+ for the transition matrix, tab delmited
'''
class HiddenMarkovModel:
    '''
    HiddenMarkovModel class that can calculate the probability
    of the hidden path
    '''
    def __init__(self,states,matrix):
        '''
        instantiates the transition matrix and states to index dictionary
        '''
        self.states = {}
        self.matrix = matrix
        for i in range(len(states)):
            self.states[states[i]] = i

    def hiddenPath(self,string):
        '''`
        calculates the probability of the string based on the transition matrix
        '''
        prob = 1/len(self.states)
        for i in range(1,len(string)):
            prob *= self.matrix[self.states[string[i-1]],self.states[string[i]]]
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
    sMatrix = []
    for i in range(5,5+len(states)):
        sMatrix.append(newLines[i].split()[1:])
    matrix = np.array(sMatrix)
    matrix = matrix.astype(np.float)
    hmm = HiddenMarkovModel(states,matrix)
    print(hmm.hiddenPath(newLines[0]))

if __name__ == '__main__':
    main()
