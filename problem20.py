#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
takes in stdin file that contains emission and transitions taken
outputs the transition matrix and emission matrix
'''
class HiddenMarkovModel:
    '''
    HMM class that computes the transition and emission matrix
    '''
    def __init__(self,emission,states):
        '''
        instantiates the emissions and states
        '''
        self.emission = emission
        self.states = states

    def estimate(self,emissions,transitions):
        '''
        computes the occurences of transition and emissions
        creates matrices for transition and emission probabilities
        '''
        occurences = {}
        for i in self.states:
            for j in self.states:
                occurences[i+j] = 0
            for k in self.emission:
                occurences[i+k] = 0
        for i in range(len(transitions)-1):
            occurences[transitions[i:i+2]] += 1
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
            if total == 0: # equal chance since none observed
                for x in range(len(tRow)):
                    tRow[x] = 1
                total = len(self.states)
            for j in range(len(tRow)):
                if tRow[j] != 0: # no divide by zero
                   tRow[j] = tRow[j]/total
            tMatrix.append(tRow)
            total = 0
            eRow = []
            for k in self.emission:
                value = occurences.get(i+k)
                total += value
                eRow.append(value)
            if total == 0:
                for x in range(len(eRow)):
                    eRow[x] = 1
                total = len(self.emission)
            for k in range(len(eRow)):
                if eRow[k] != 0:
                   eRow[k] = eRow[k]/total
            eMatrix.append(eRow)
        return (tMatrix,eMatrix) # man this code is unnecessarily long

def main():
    '''
    formats the input into the emissions and transitions
    print formats to tabs between matrix values
    creates the object and runs the estimation of parameters
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    states = newLines[6].split()
    emission = newLines[2].split()
    hmm = HiddenMarkovModel(emission,states)
    matrices = hmm.estimate(newLines[0],newLines[4])
    print('\t' + '\t'.join(newLines[6]))
    for i in range(len(states)):
        line = '\t'.join(str(x) for x in matrices[0][i])
        print(states[i] + '\t' + line)
    print('--------')
    print('\t' + '\t'.join(newLines[2]))
    for i in range(len(states)):
        line = '\t'.join(str(x) for x in matrices[1][i])
        print(states[i] + '\t' + line)

if __name__ == '__main__':
    main()   
