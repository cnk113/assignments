#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

'''
This program takes in from stdin the peptide string
Outputs the cyclospectrum of the cyclic peptide to stdout
'''

class Spectrum:
    '''
    The Spectrum class has a class dictionary for all amino acid masses
    functions to calcualte the cyclospectrum of a given peptide
    '''
    masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    def __init__(self):
        '''
        instantiates the cyclospectrum of this object
        '''
        self.spectrum = [0]

    def combinations(self,seq):
        '''
        creates all constituents of the cyclic peptide
        to compute the cyclospectrum
        returns the sorted cyclospectrum
        '''
        cyclic = seq*2 # Allows to find the subsequences of cyclopeptide by wrapping around
        peptides = [seq]
        for i in range(len(seq)):
            for j in range(1,len(seq)):
                peptides.append(cyclic[i:i+j])
        for peptide in peptides:
            spec = 0
            for aa in peptide:
                spec += self.masses.get(aa)
            self.spectrum.append(spec)
        return sorted(self.spectrum)

def main():
    '''
    takes in from stdin the peptide and
    creates the Spectrum oject to
    print to stdout the cyclospectrum
    '''
    protein = sys.stdin.readlines()[0]
    spec = Spectrum()
    peptides = spec.combinations(protein.rstrip())
    print(' '.join(str(m) for m in peptides)) 

if __name__ == "__main__":
    main()
