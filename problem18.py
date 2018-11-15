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
    def __init__(self,emissions,states,sM,eM):
        '''
        sets the class variables:
        emission matrix, state matrix, state dict of the index to label, emission dict of label to index
        '''
        self.tMatrix = sM.astype(np.float)
        self.eMatrix = eM.astype(np.float)
        self.states = {}
        self.emissions = {}
        self.back = {}
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
        for i in range(1,len(string)):
            for j in range(len(self.states)):
                temp = []
                for k in range(len(self.states)):
                    temp.append(dag[k,i-1] * self.tMatrix[k,j])
                dag[j,i] = max(temp) * self.eMatrix[j,self.emissions.get(string[i])]
                self.back[dag[j,i]] = temp.index(max(temp))
        p = [dag[:,len(string)-1].argmax(axis=0)]
        current = dag[:,i].max()
        for i in range(len(string)-1,0,-1):
            row = self.back.get(current)
            p.append(row)
            current = dag[row,i]
        return p[::-1]

    def decoder(self,string):
        '''
        Input: list of indices of the rows
        Output: translates the indices to states
        '''
        decoded = ''
        for i in string:
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
    states = newLines[2].split()
    emissions = newLines[4].split()
    a = newLines[7].split('\t')
    b = newLines[8].split('\t')
    c = newLines[11].split('\t')
    d = newLines[12].split('\t')
    statesMatrix = np.array([a[1:],b[1:]])
    emissionsMatrix = np.array([c[1:],d[1:]])
    hmm = Viterbi(states,emissions,statesMatrix,emissionsMatrix)
    print(hmm.decoder(hmm.path(newLines[0])))

if __name__ == "__main__":
    main()
