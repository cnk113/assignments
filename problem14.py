#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes in stdin of a collection of kmers of size k
Outputs to stdout the reconstructed string
reconstructs in linear time
'''

class StringReconstruction:
    '''
    StringReconstruction class creates a graph of kmers
    allows traversal in linear time to reconstruct string
    '''
    def __init__(self,seq):
        '''
        initialzies the adjacency list and indegrees dict
        '''
        self.kmers = seq
        self.adj = {}
        self.inDegree = {}

    def deBrujin(self):
        '''
        constructs the adjacency list of a deBrujin graph
        also calculates the indegrees of all nodes
        '''
        for kmer in self.kmers:
            prefix = kmer[:-1]
            suffix = kmer[1:]
            self.adj[prefix] = suffix
            self.inDegree[prefix] = 0 # to get all edge case nodes
            self.inDegree[suffix] = 0 # to get all edge case nodes
        for key in self.adj:
            self.inDegree[self.adj.get(key)] += 1

    def start(self):
        '''
        gets the starting kmer which has an indegree value of 0
        returns start node
        '''
        for key in self.adj:
            if self.inDegree[key] == 0:
                return key

    def reconstruct(self):
        '''
        reconstructs the string in linear time by using adjacency list
        to access the next kmer and returns string
        '''
        self.deBrujin()
        current = self.start()
        visited = []
        while current != None:
            visited.append(current)
            current = self.adj.get(current)
        string = visited[0]
        for kmer in visited[1:]:
            string += kmer[-1] # appends the last char of each string after first
        return string

def main():
    '''
    takes in input file from stdin and strips newlines
    constructs the StringReconstruction object and reconstructs the string
    outputs to stdout the reconstructed string
    '''
    lines = sys.stdin.readlines()
    newLines = []
    for seq in lines:
        newLines.append(seq.rstrip()) # removes newlines
    string = StringReconstruction(newLines[1:])
    print(string.reconstruct())

if __name__ == '__main__':
    main()
