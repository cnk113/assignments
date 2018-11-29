#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
program takes in stdin file with the necessary informtion such as transition and emission matrices
to be able to compute a hidden path take by the emission
prints out the most likely hidden path taken
'''
class Viterbi:
    '''
    Implementation of the Viterbi algorithm
    Input: emission matrix, state matrix, emissions, and states
    Output: hidden path
    '''
    def __init__(self,states,emissions,sM,eM):
        '''
        sets the class variables:
        emission matrix, state matrix, state dict of the index to label, emission dict of label to index
        '''
        self.tMatrix = sM.astype(np.float)
        self.eMatrix = eM.astype(np.float)
        self.states = {}
        self.emissions = {}
        for i in range(len(states)):
            self.states[i] = states[i]
        for i in range(len(emissions)):
            self.emissions[emissions[i]] = i

    def path(self,string):
        '''
        finds the hidden path taken by the input string
        backtracks and returns the hidden path taken
        '''
        dag = np.zeros((len(self.states),len(string)))
        for i in range(len(self.states)):
            dag[i,0] = self.eMatrix[i,self.emissions.get(string[0])]
        back = {}
        for i in range(1,len(string)):
            for j in range(len(self.states)):
                temp = []
                for k in range(len(self.states)):
                    temp.append(dag[k,i-1] * self.tMatrix[k,j])
                dag[j,i] = max(temp) * self.eMatrix[j,self.emissions.get(string[i])]
                back[dag[j,i]] = temp.index(max(temp))
        p = [dag[:,len(string)-1].argmax(axis=0)]
        current = dag[:,len(string)-1].max()
        for i in range(len(string)-2,-1,-1):
            row = back.get(current)
            p.append(row)
            current = dag[row,i]
        p[::-1]
        decoded = ''
        for i in p:
            decoded += self.states[i]
        return decoded

    def maximize(self,string):
        '''
        '''
        occurences = {}
        for i in self.states:
            for j in self.states:
                occurences[i+j] = 0
            for k in self.emission:
                occurences[i+k] = 0
        for i in range(len(transitions)-1):
            occurences[transitions[i:i+1]] += 1
        for i in range(len(emissions)):
            occurences[transitions[i]+emissions[i]] += 1
        tMatrix = []
        eMatrix = []
        for i in self.states:
            total = 0
            tRow = []
            for j in self.states:
                value = occurences.get(i+j)
                total += value
                tRow.append(value)
            divided = [x / total for x in tRow]
            tMatrix.append(divided)
            total = 0
            eRow = []
            for k in self.emission:
                value = occurences.get(i+k)
                total += value
                eRow.append(value)
            divided = [x / total for x in eRow]
            eMatrix.append(divided)
        return (tMatrix,eMatrix)

def main():
    '''
    parses the stdin file and creates numpy matrices of the emissions and states
    creates the Viterbi object and runs the functions
    Input: file (through stdin)
    Output: the hidden path
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    emissions = newLines[2].split()
    states = newLines[4].split()
    sMatrix = []
    eMatrix = []
    for i in range(9,9+len(states)):
        sMatrix.append(newLines[i].split('\t')[1:])
    for i in range(11+len(states),11+2*len(states)):
        eMatrix.append(newLines[i].split('\t')[1:])
    statesMatrix = np.array(sMatrix)
    emissionsMatrix = np.array(eMatrix)
    hmm = Viterbi(states,emissions,statesMatrix,emissionsMatrix)

if __name__ == "__main__":
    main()