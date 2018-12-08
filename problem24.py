#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

class EncodedProtein:
    '''
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
        '''
        self.peptide = peptide

    def coordinates(self,string):
        '''
        '''
        start = []
        stop = []
        for i in range(3):
            for j in range(i,len(self.seq)-i,3):
                protein = dnaCodonTable.get(self.seq[j:j+3])
                if protein == 'M' and len(start) == len(stop):
                    start.append(j)
                elif protein == '-' and len(start) == len(stop)+1:
                    stop.append(j)
        return (start,stop)

    def translatedFrames(self,seq,coord):
        start = coord[0]
        stop = coord[1]
        allProteins = []
        for i in range(len(stop)):
            proteins = []
            for j in range(start[i],stop[i],3):
                proteins.append(dnaCodonTable.get(seq[j:j+3]))
            allProteins.append(proteins)
        for i in range(0,len(allProteins),len(peptide)):
            if peptide == proteins[i:i+len(peptide)]:


    def forwardReverse(self,string):
        '''
        '''
        readingFrames = self.coordinates(string)
        complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        reverseReadingFrames = self.coordinates(''.join(complement[i] for i in string[::-1]))

        

def main():
    '''
    '''
    lines = sys.stdin.readlines()
    encoded = EncodedProtein(lines[1].rstrip)())
    encoded.forwardReverse(lines[0].rstrip())


if __name__ == "__main__":
    main()
