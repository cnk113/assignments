#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
Takes in the stdin file and parses for the transition and emission matrix
file should have input emission string as the first line
emissions on line 3, states on line 7 both are space delimited
matrix on line 10+ tab delimited
'''
class HiddenMarkovModel:
    '''
    HiddenMarkovModel class that finds probability of emission
    based on transitions
    '''
    def __init__(self,emissions,states,matrix):
        '''
        instantiates the emissions matrix, dictionary of states and emissions to index values of the matrix
        '''
        self.values = {}
        self.matrix = matrix
        for i in range(len(states)):
            self.values[states[i]] = i
        for i in range(len(emissions)):
            self.values[emissions[i]] = i

    def hiddenPath(self,string,transition):
        '''
        Input: string, emissions, states, transition matrix
        Output: probability of the emission based on the transition states
        '''
        prob = self.matrix[self.values.get(transition[0]),self.values.get(string[0])]
        for i in range(1,len(string)):
            prob *= self.matrix[self.values.get(transition[i]),self.values.get(string[i])]
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
    emissions = newLines[2].split()
    states = newLines[6].split()
    matrix = []
    for i in range(9,9+len(states)):
        matrix.append(newLines[i].split()[1:])
    emissionsMatrix = np.array(matrix)
    emissionsMatrix = emissionsMatrix.astype(np.float)
    hmm = HiddenMarkovModel(emissions,states,emissionsMatrix)
    print(hmm.hiddenPath(newLines[0],newLines[4]))

if __name__ == '__main__':
    main()
