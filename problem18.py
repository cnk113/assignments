#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

class Viterbi:
    '''
    '''
    def __init__(self,emissions,states,sM,eM):
        '''
        '''
        self.tMatrix = sM.astype(np.float)
        self.eMatrix = eM.astype(np.float)
        self.states = {}
        self.emissions = {}
        self.path = {}
        for i in range(len(states)):
            self.states[i] = states[i]
        for i in range(len(emissions)):
            self.emissions[emissions[i]] = i

    def path(self,string):
        '''
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
                self.path[dag[j,i]] = temp.index(max(temp))
        p = [dag[:,len(string)-1].argmax(axis=0)]
        for i in range(len(string)-1,0,-1):
            current = dag[:,i].max()
            row = self.path.get(current)
            p.append(row)
        print(p)
        return p[::-1]

    def decoder(self,string):
        '''
        '''
        decoded = ''
        for i in string:
            decoded += self.states[i]
        return decoded

def main():
    '''
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
