#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
'''
class HiddenMarkovModel:
    '''
    '''
    def __init__(self,emission,states):
        '''
        '''
        self.emission = emission
        self.states = states

    def estimate(emissions,transitions):
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
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for line in lines:
        newLines.append(line.rstrip())
    states = newLines[2].split()
    emission = newLines[6].split()
    hmm = HiddenMarkovModel(emission,states)
    matrices = hmm.estimate(newLines[0],newLines[4])
    print(newLines[6])
    for i in range(len(states)):
        line = ''.join(for value in matrices[0])
        print(states[i] + '\t' + 
    print('--------')
    print(newLines[2])
    for row in matrices[1]:


if __name__ == '__main__':
    main()   
