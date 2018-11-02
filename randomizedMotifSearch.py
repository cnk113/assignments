#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import fastaReader
import argparse
import random
import numpy as np
import math
random.seed(42)

'''
Input: STDIN FASTA, pseudocounts, iterations, kmer length, sequences of consensus motifs
Output: STDOUT Consensus string and score
Finds the motif by searching for a local minima based on an entropy score and a random beginning
Repeats the above process by N iterations
'''
class MotifSearch:
    '''
    Creates a class that runs randomizedMotifSearch with parameters of iteration, kmer length, and pseudocounts
    '''
    def __init__(self, seq, pseudo, length):
        '''
        constructor that sets class variables which are the sequences, pseudocounts, and kmer length
        '''
        self.seq = seq
        self.pseudo = pseudo
        self.k = length

    def score(self, motif):
        '''
        returns a tuple of the score and consensus
        no need for a for loop in iterating over the rows since there are always 4 rows for ACGT
        '''
        d = {0:'A', 1:'C', 2:'G', 3:'T'} # rows of profile
        prof = self.profile(motif) # gets profile matrix of the motifs
        total = 0
        kmer = ''
        for i in range(len(motif[0])): # iterate over columns
            ent = 0
            for j in range(4):
                ent += (prof[j,i] * math.log(prof[j,i],2.0))
            total += (-1 * ent)
            highest = np.argmax(prof[:,i]) # index of the highest probability base in the column, first one found is returned
            kmer += d.get(highest) # adds the most probable base to get the consensus
        return(total,kmer,motif)

    def randomKmers(self):
        '''
        returns a list of random kmers from each sequence
        '''
        motifs = []
        for s in self.seq:
            pos = random.randint(0,len(s)-self.k)
            motifs.append(s[pos:pos+self.k])
        return motifs

    def motifProfile(self, profile):
        '''
        returns a list of best probable kmers from each sequence from given profile
        '''
        d = {'A':0, 'C':1, 'G':2, 'T':3} # rows of profile
        bestKmers = []
        for seq in self.seq: # for each string
            best = 0 
            for pos in range(len(seq)-self.k+1): # each kmer within that string of a length K
                kmer = seq[pos:pos+self.k]
                pr = 1 # probability of the kmer
                j = 0 # column number or base letter
                for base in kmer:
                    pr *= profile[d.get(base),j] # calculates probability of the kmer from profile matrix
                    j += 1
                if pr > best: # checks if kmer is more probable
                    best = pr
                    bestKmer = kmer
            bestKmers.append(bestKmer)
        return bestKmers

    def profile(self, motif):
        '''
        returns profile matrix from the given motifs with pseudocounts
        no need for a for loop in iterating over the rows since there are always 4 rows for ACGT
        '''
        n = {0:'A', 1:'C', 2:'G', 3:'T'} # rows of profile
        m = np.asarray([list(kmer) for  kmer in motif])
        prof = np.zeros((4,len(motif[0])))
        prof.fill(self.pseudo) # fills profile with the pseudocounts
        for i in range(len(motif[0])):
            key, count = np.unique(m[:,i], return_counts=True) # gets ALL counts
            d = dict(zip(key,count))
            for j in range(4):    
                prof[j,i] += d.get(n.get(j),0)
        return prof/(len(motif)+self.pseudo*4) # divides by total to calculate probability 

    def randomizedMotifSearch(self):
        '''
        returns a tuple of the motif and the score based on entropy, based on pseudocode from textbook
        '''
        bestMotifs = self.randomKmers()
        best = self.score(bestMotifs)
        while True:
            profile = self.profile(bestMotifs)
            newMotifs = self.motifProfile(profile)
            new = self.score(newMotifs)
            if new[0] < best[0]:
                best = new
                bestMotifs = newMotifs
            else:
                return best

    def run(self,m,n):
        '''
        runs the randomized motif search N times and prints out the best score and consensus
        '''
        bestMotif = self.randomizedMotifSearch()
        for i in range(n-1):
            motif = self.randomizedMotifSearch()
            if motif[0] < bestMotif[0]: # checks for lowest score
                bestMotif = motif
        print(bestMotif[1] + " " + str(bestMotif[0]))
        if m: # sequences of the consensus
            for seq in bestMotif[2]:
                print(seq)

def parse_args():
    '''
    argument parser for this program
    -i,-k,-p is required and include -m if you want the motifs of the consensus
    '''
    parser = argparse.ArgumentParser(description = 'Takes in a FASTA file, kmer length, pseudocount, number of iterations, and outputs the consensus sequences')
    parser.add_argument('-i', type=int, help='number of iterations of runs for randomizedMotifSearch')
    parser.add_argument('-p', type=int, help='number of pseudocount to fill in')
    parser.add_argument('-k', type=int, help='kmer length')
    parser.add_argument('-m', action='store_true', default=False, help='displays sequences used to build the best consensus')
    return parser.parse_args()

def main():
    '''
    initializes the objects, takes in arguments, and runs the class functionalities
    '''
    opts = parse_args()
    reader = fastaReader.FastAreader()
    seqs = []
    for head, seq in reader.readFasta():
        seqs.append(seq)
    motif = MotifSearch(seqs,opts.p,opts.k)
    motif.run(opts.m,opts.i)

if __name__ == "__main__":
    main()