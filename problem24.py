#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes in from stdin the DNA string and an amino acid string both seperated by newlines
OUtputs reading frames that encode the given protein delimited by new lines
does not take into account stop codons
'''

class EncodedProtein:
    '''
    EncodedProtein class has 2 class dictionaries the codon tables for RNA to amino acid
    and DNA to amino acid
    '''
    rnaCodonTable = {
    # RNA codon table
    # U
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',  # UxU
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',  # UxC
    'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',  # UxA
    'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',  # UxG
    # C
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',  # CxU
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',  # CxC
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',  # CxA
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',  # CxG
    # A
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',  # AxU
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',  # AxC
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',  # AxA
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',  # AxG
    # G
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',  # GxU
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',  # GxC
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',  # GxA
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
    }
    dnaCodonTable = {key.replace('U','T'):value for key, value in rnaCodonTable.items()}
    def __init__(self,peptide):
        '''
        takes in the peptide to search for in the DNA sequence
        '''
        self.peptide = peptide

    def substrings(self,seq):
        '''
        takes in the DNA sequence and searches for all possible frames that translate to the protein
        returns all frames seperated by newlines
        '''
        complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        k = len(self.peptide)*3
        frames = ''
        for i in range(len(seq)-k+1):
            frame = seq[i:i+k]
            reverse = ''.join(complement[i] for i in frame[::-1])
            if self.translate(frame) == self.peptide or self.translate(reverse) == self.peptide:
                frames += frame + '\n'
        return frames.rstrip()

    def translate(self,seq):
        '''
        takes in a substring of the DNA sequence to translate to the amino acid using the table
        returns the amino acid
        '''
        aa = ''
        for i in range(0,len(seq),3):
            aa += self.dnaCodonTable.get(seq[i:i+3])
        return aa

def main():
    '''
    takes in the input from stdin and create the class
    creates the EncodedProtein class and prints out the frames by newlines
    '''
    lines = sys.stdin.readlines()
    encoded = EncodedProtein(lines[1].rstrip())
    print(encoded.substrings(lines[0].rstrip()))

if __name__ == "__main__":
    main()
