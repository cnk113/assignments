#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
Input: text file with emission matrix, transition matrix, states, emissions (through stdin)
Output: probability of the transition state probability at each position in the emission
'''
class HiddenMarkovModel:
    '''
    Hidden Markov Model object with class variables with:
    emission matrix, transition matrix, states, emissions
    Input: emissions
    Output: probability of the transitions at each state
    '''
    def __init__(self,emissions,states,sM,eM):
        '''
        sets the class variables of the matrices, states, and emissions
        also sets up the emissions to the indices of the emission matrix
        '''
        self.tMatrix = sM
        self.eMatrix = eM
        self.states = states
        self.emissions = {}
        for i in range(len(emissions)):
            self.emissions[emissions[i]] = i

    def softDecoder(self,string):
        '''
        takes in the emission and calculates the probability of the transition state
        at each position of the emitted string
        '''
        forward = np.zeros((len(self.states),len(string)))
        for i in range(len(self.states)): # initializes first column
            forward[i,0] = self.eMatrix[i,self.emissions.get(string[0])]
        for i in range(1,len(string)): # column
            for j in range(len(self.states)): # row
                prod = 0
                for k in range(len(self.states)): # previous column
                    prod += forward[k,i-1] * self.tMatrix[k,j] # USE DOT PRODUCTS
                forward[j,i] = prod * self.eMatrix[j,self.emissions.get(string[i])]
        backward = np.zeros((len(self.states),len(string)))
        for i in range(len(self.states)): # initializes first column
            backward[i,-1] = self.eMatrix[i,self.emissions.get(string[-1])]
        for i in range(len(string)-2,-1,-1): # column
            for j in range(len(self.states)): # row
                prod = 0
                for k in range(len(self.states)): # previous column
                    prod += backward[k,i+1] * self.tMatrix[j,k] # I should probabily use dot products
                backward[j,i] = prod * self.eMatrix[j,self.emissions.get(string[i])]
        nodeMatrix = np.zeros((len(self.states),len(string)))
        sink = np.sum(forward[:,len(string)-1],axis=0)
        for i in range(len(string)):
            for j in range(len(self.states)):
                nodeMatrix[j,i] = (forward[j,i] * backward[j,i]) / (sink * self.eMatrix[j,self.emissions.get(string[i])])
        return nodeMatrix.tolist()

def main():
    '''
    parses the input file and creates a HiddenMarkovModel object
    computes the transition probabilities and
    prints out the probability of the transition state at each position of emission
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    emissions = newLines[2].split()
    states = newLines[4].split()
    sMatrix = []
    eMatrix = []
    for i in range(7,7+len(states)):
        sMatrix.append(newLines[i].split()[1:])
    for i in range(9+len(states),9+2*len(states)):
        eMatrix.append(newLines[i].split()[1:])
    statesMatrix = np.array(sMatrix)
    emissionsMatrix = np.array(eMatrix)
    hmm = HiddenMarkovModel(emissions,states,statesMatrix.astype(np.float),emissionsMatrix.astype(np.float))
    matrix = hmm.softDecoder(newLines[0])
    print('\t'.join(states))
    for i in range(len(matrix[0])):
        print('\t'.join(str(row[i]) for row in matrix))


if __name__ == '__main__':
    main()
