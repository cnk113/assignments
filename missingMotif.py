#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import argparse
import math
import fastaReader
from scipy.stats import binom

'''
Input: FASTA file, optional: minMotif,maxMotif, and cutoff
Output: kmers and their respective statistics
Looks for motifs that have been significantly unrepresented by a null distribution
'''
class Motifs:
    '''
    Motifs class
    takes in DNA string and the sizes of kmers to find and filters to a statistical cutoff
    '''
    def __init__(self, mn, mx, c, t):
        '''
        constructor and sets the class instances
        '''
        self.min = mn
        self.max = mx
        self.cutoff = c 
        self.fasta = t
        self.count = {}
        self.exp = {}
        self.z = {}
        self.p = {}

    def reverseComplement(self,kmer):
        '''
        returns the reverse complement of the kmer
        '''
        complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        return ''.join(complement[i] for i in kmer[::-1])

    def kmerParse(self):
        '''
        counts all the kmers and save the kmer and the count to the dictionary
        '''
        for kmerSize in range(self.min-2,self.max+1):
            for pos in range(len(self.fasta)-kmerSize+1):
                kmer = self.fasta[pos:pos+kmerSize]
                if 'N' in kmer:
                    continue
                rev = self.reverseComplement(kmer)
                if kmer not in self.count: # Not a palindrome
                    self.count[kmer] = 1
                    self.count[rev] = 1
                elif kmer == rev: # Is a palindrome
                    self.count[kmer] += 1
                else:
                    self.count[kmer] += 1
                    self.count[rev] += 1

    def zScore(self):
        '''
        calulates the expected value of each kmer along with the average and
        std devation to calculate the z score which is saved in a dictionary
        '''
        for kmer in self.count:
            if len(kmer)>=self.min:
                if len(kmer) < 3:
                    continue
                exp = (self.count[kmer[1:]]*self.count[kmer[:-1]])/self.count[kmer[1:-1]] # mean
                sd = math.sqrt(exp*(1-exp/len(self.fasta)))
                z = (self.count.get(kmer)-exp)/sd
                self.exp[kmer] = exp
                self.z[kmer] = z

    def printKmers(self):
        '''
        prints out the filtered kmers and other attributes sorted by p value in increasing value 
        NOTE: if you're wondering why the printing takes long it is because the p value is calculated as it prints
        This is faster to calculate since only half the kmers are being calculated as the reverse complemented is filtered out in the same process
        '''
        tup = sorted(self.z.items(), key=lambda x: (x[1])) # sorts by z score
        tup = sorted(tup, key=lambda x: len(x[0]), reverse=True) # sorts by kmer length
        for k, v in tup:
            if v <= self.cutoff: # Checks for cutoff zscore
                rev = self.reverseComplement(k)
                x = k
                if rev < k: # sorts alphabetically
                    x = rev
                    y = k
                else:
                    y = rev
                tup.remove((y,v)) # remove the duplicate reverse complements from dictionary
                print('{0:8}:{1:8}\t{2:0d}\t{3:0.2f}\t{4:0.2f}\t{5:0.2e}'.format(x, y, self.count.get(k), self.exp.get(k), v, binom.cdf(self.count.get(k),len(self.fasta),self.exp.get(k)/len(self.fasta))))

def parse_args():
    '''
    argument parser for this program
    '''
    parser = argparse.ArgumentParser(description = 'Finds all possible kmers within a given range and filters based on size of kmer and statistical significance')
    parser.add_argument('--minMotif', type=int, default=3, help='minimum motif length for statisical analysis')
    parser.add_argument('--maxMotif', type=int, default=8, help='maximum motif length for statisical analysis')
    parser.add_argument('--cutoff', type=int, default=-3, help='statistical value for cutoff')
    return parser.parse_args()

def main():
    '''
    creates the Motif class which allows it to parse the fasta and outputs the results from analysis
    '''
    opts = parse_args()
    reader = fastaReader.FastAreader()
    for head, seq in reader.readFasta():
        motif = Motifs(opts.minMotif, opts.maxMotif, opts.cutoff, seq)
        motif.kmerParse()
        motif.zScore()
        print('N = ' + str(len(seq)))
        motif.printKmers()

if __name__ == "__main__":
    main()
