#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
Input: text file with iterations, emission matrix, transition matrix, states, emissions (through stdin)
Output: new transition and emission matrices through Baum Welch learning over given iterations
'''
class HiddenMarkovModel:
    '''
    Hidden Markov Model object with class variables with:
    transition states, emissions
    implements Baum Welch learning
    '''
    def __init__(self,emissions,states):
        '''
        sets the class variables of the matrices, states, and emissions
        also sets up the emissions to the indices of the emission matrix
        '''
        self.states = states
        self.emissions = emissions
        self.emissionDict = {}
        for i in range(len(emissions)):
            self.emissionDict[emissions[i]] = i
        self.edgePair = {} # Used in edge responsibility matrix
        pairs = []
        for i in range(len(states)):
            for j in range(len(states)):
                pairs.append(str(i)+str(j))
        for i in range(len(pairs)):
            self.edgePair[pairs[i]] = i

    def maximization(self,string,matrices):
        '''
        recomputes the matrices by maximizing over the node and edge responsibility matrix
        '''
        nodeMatrix = matrices[0]
        eMatrix = np.zeros((len(self.states),len(self.emissions)))
        for i in range(len(self.states)):
            for j in range(len(self.emissions)):
                prob = 0
                for k in range(len(string)):
                    if string[k] == self.emissions[j]: # Too lazy to make dictionary for optimization
                        prob += nodeMatrix[i,k]
                eMatrix[i,j] = prob 
        eMatrix = (eMatrix.T/eMatrix.sum(axis=1)).T # Divides by total
        edgeMatrix = matrices[1]
        tMatrix = np.zeros((len(self.states),len(self.states)))
        for i in range(len(self.states)):
            for j in range(len(self.states)):
                prob = 0
                for k in range(len(string)):
                    prob += edgeMatrix[self.edgePair.get(str(i)+str(j)),k]
                tMatrix[i,j] = prob
        tMatrix = (tMatrix.T/tMatrix.sum(axis=1)).T
        return (eMatrix,tMatrix)

    def expectation(self,string,matrices):
        '''
        calculates the node and edge matrices by the expected valueof the emitted string given from the emission
        and tranisition matrices
        '''
        tMatrix = matrices[1]
        eMatrix = matrices[0]
        forward = np.zeros((len(self.states),len(string)))
        for i in range(len(self.states)): # initializes first column
            forward[i,0] = eMatrix[i,self.emissionDict.get(string[0])]
        for i in range(1,len(string)): # column
            for j in range(len(self.states)): # row
                prod = 0
                for k in range(len(self.states)): # previous column
                    prod += forward[k,i-1] * tMatrix[k,j] # sum the products of prev column
                forward[j,i] = prod * eMatrix[j,self.emissionDict.get(string[i])]
        backward = np.zeros((len(self.states),len(string)))
        for i in range(len(self.states)): # initializes first column
            backward[i,-1] = eMatrix[i,self.emissionDict.get(string[-1])]
        for i in range(len(string)-2,-1,-1): # column
            for j in range(len(self.states)): # row
                prod = 0
                for k in range(len(self.states)): # previous column
                    prod += backward[k,i+1] * tMatrix[j,k] # sum the products of prev column
                backward[j,i] = prod * eMatrix[j,self.emissionDict.get(string[i])]
        total = np.sum(forward[:,len(string)-1],axis=0)
        nodeMatrix = np.zeros((len(self.states),len(string)))
        for i in range(len(string)):
            for j in range(len(self.states)):
                nodeMatrix[j,i] = (forward[j,i] * backward[j,i] / (total * eMatrix[j,self.emissionDict.get(string[i])]))
        edgeMatrix = np.zeros((len(self.states)**2,len(string)))
        for i in range(len(string)-1):
            for j in range(len(self.states)):
                for k in range(len(self.states)):
                    edgeMatrix[self.edgePair.get(str(j)+str(k)),i] = forward[j,i] * backward[k,i+1] * tMatrix[j,k] / total
        return (nodeMatrix,edgeMatrix)

    def baumWelchLearning(self,string,eMatrix,sMatrix,num):
        '''
        runs the Baum Welch algorthim a given number of times
        returns the matrices after the iterations
        '''
        matrices = (eMatrix,sMatrix)
        for i in range(int(num)):
            matrices = self.maximization(string,self.expectation(string,matrices))
        return matrices

def main():
    '''
    parses the input file and creates a HiddenMarkovModel object
    runs the EM algorithm by the given iteration value
    prints out the newly trained matrices using Baum Welch learning
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    emissions = newLines[4].split()
    states = newLines[6].split()
    sMatrix = []
    eMatrix = []
    for i in range(9,9+len(states)):
        sMatrix.append(newLines[i].split()[1:])
    for i in range(11+len(states),11+2*len(states)):
        eMatrix.append(newLines[i].split()[1:])
    statesMatrix = np.array(sMatrix).astype(np.float)
    emissionsMatrix = np.array(eMatrix).astype(np.float)
    hmm = HiddenMarkovModel(emissions,states)
    matrices = hmm.baumWelchLearning(newLines[2],emissionsMatrix,statesMatrix,newLines[0])
    print('\t' + '\t'.join(states))
    tMatrix = matrices[1].tolist()
    for i in range(len(states)):
        values = '\t'.join(str(x) for x in tMatrix[i])
        print(states[i] + '\t' + values)
    print('--------')
    print('\t' + '\t'.join(emissions))
    eMatrix = matrices[0].tolist()
    for i in range(len(states)):
        values = '\t'.join(str(x) for x in eMatrix[i])
        print(states[i] + '\t' + values)

if __name__ == '__main__':
    main()
