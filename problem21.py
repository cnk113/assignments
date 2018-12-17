#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
import numpy as np

'''
program takes in stdin file with the necessary informtion such as transition and emission matrices
to be able to compute a hidden path take by the emission
prints out the emission and transition matrix of maximized probability of all hidden paths
'''
class Viterbi:
    '''
    Implementation of the Viterbi algorithm
    Input: emission matrix, state matrix, emissions, and states
    Output: emission and transition matrices
    '''
    def __init__(self,states,emissions):
        '''
        sets the class variables:
        emission matrix, state matrix, state dict of the index to label, emission dict of label to index
        '''
        self.states = states
        self.emission = emissions
        self.stateDict = {}
        self.emissionDict = {}
        for i in range(len(states)):
            self.stateDict[i] = states[i]
        for i in range(len(emissions)):
            self.emissionDict[emissions[i]] = i

    def path(self,string,matrices):
        '''
        finds the hidden path taken by the input string
        backtracks and returns the hidden path taken
        '''
        tMatrix = matrices[0]
        eMatrix = matrices[1]
        dag = np.zeros((len(self.states),len(string)))
        for i in range(len(self.states)):
            dag[i,0] = eMatrix[i,self.emissionDict.get(string[0])]
        back = {} # back pointer
        for i in range(1,len(string)):
            for j in range(len(self.states)):
                temp = []
                for k in range(len(self.states)):
                    temp.append(dag[k,i-1] * tMatrix[k,j])
                dag[j,i] = max(temp) * eMatrix[j,self.emissionDict.get(string[i])]
                back[str(j)+str(i)] = temp.index(max(temp))
        sink = dag[:,len(string)-1].argmax(axis=0)
        current = str(sink)+str(len(string)-1)
        p = [sink]
        for i in range(len(string)-2,-1,-1): # backtrack
            row = back.get(current)
            p.append(row)
            current = str(row)+str(i)
        return (''.join(self.stateDict[i] for i in p[::-1])) # translates the indices of transition matrix to transition state

    def estimate(self,emissions,transitions):
        '''
        calculates the emission and transition matrices by maximizing over
        probability over all hidden paths
        SORRY FOR THE SPAGHETTI CODE
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
            if total == 0:
                for x in range(len(tRow)):
                    tRow[x] = 1
                total = len(self.states)
            for j in range(len(tRow)):
                if tRow[j] != 0:
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
        return(np.array(tMatrix),np.array(eMatrix))

    def viterbiLearning(self,string,sMatrix,eMatrix,num):
        '''
        runs viterbi learning over a given number of iterations
        returns the transition and emission matrix of the resulting iterations
        '''
        matrices = (sMatrix,eMatrix)
        for i in range(int(num)):
            matrices = self.estimate(string,self.path(string,matrices))
        return matrices

def main():
    '''
    parses the stdin file and creates numpy matrices of the emissions and states
    creates the Viterbi object and runs the functions
    Input: file (through stdin)
    Output: prints transition and emission matrices
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
    hmm = Viterbi(states,emissions)
    matrices = hmm.viterbiLearning(newLines[2],statesMatrix,emissionsMatrix,newLines[0])
    print('\t' + '\t'.join(states))
    for i in range(len(states)):
        line = '\t'.join(str(x) for x in matrices[0][i])
        print(states[i] + '\t' + line)
    print('--------')
    print('\t' + '\t'.join(emissions))
    for i in range(len(states)):
        line = '\t'.join(str(x) for x in matrices[1][i])
        print(states[i] + '\t' + line)

if __name__ == "__main__":
    main()
