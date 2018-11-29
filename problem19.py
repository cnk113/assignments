#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
Input: text file with emission matrix, transition matrix, states, emissions (through stdin)
Output: probability of the emission
program computes the probability of the emission based on all possible paths taken
prints out the probability
'''
class HiddenMarkovModel:
    '''
    Hidden Markov Model object with class variables with:
    emission matrix, transition matrix, states, emissions
    Input: emissions
    Output: probability of the input
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

    def emissionProbability(self,string):
        '''
        takes in the emission and calculates the probability of the emission
        sums up the preceding states for the score of the current node
        uses dynamic programming
        '''
        dag = np.zeros((len(self.states),len(string)))
        for i in range(len(self.states)): # initializes first column
            dag[i,0] = self.eMatrix[i,self.emissions.get(string[0])]
        for i in range(1,len(string)): # column
            for j in range(len(self.states)): # row
                prod = 0
                for k in range(len(self.states)): # previous column
                    prod += (dag[k,i-1] * self.tMatrix[k,j]) # sum the products of prev column
                dag[j,i] = prod * self.eMatrix[j,self.emissions.get(string[i])]
        return np.sum(dag[:,len(string)-1],axis=0)/len(self.states) # gets the sum of last column or probability of the entire emission

def main():
    '''
    parses the input file and creates a HiddenMarkovModel object
    prints out the probability of the emission string
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
    print(hmm.emissionProbability(newLines[0]))


if __name__ == '__main__':
    main()
