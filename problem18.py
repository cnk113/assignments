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
        self.tMatrix = sM
        self.eMatrix = eM
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
        back = {} # back pointer
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
        p = p[::-1]
        decoded = ''
        for i in p:
            decoded += self.states[i]
        return decoded

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
    for i in range(7,7+len(states)):
        sMatrix.append(newLines[i].split()[1:])
    for i in range(9+len(states),9+2*len(states)):
        eMatrix.append(newLines[i].split()[1:])
    statesMatrix = np.array(sMatrix)
    statesMatrix = statesMatrix.astype(np.float)
    emissionsMatrix = np.array(eMatrix)
    emissionsMatrix = emissionsMatrix.astype(np.float)
    hmm = Viterbi(states,emissions,statesMatrix,emissionsMatrix)
    print(hmm.path(newLines[0]))

if __name__ == "__main__":
    main()
