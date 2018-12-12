#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
from collections import Counter

'''
This program takes from stdin of a cyclopeptide's cyclospectrum
Outputs to stdout all the combinations of the cyclopeptides masses
'''

class Peptide:
    '''
    Peptide class that has all masses of amino acids
    functions to calculate the cyclopeptide based on the cyclospectrum
    '''
    masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'N': 114,'D': 115, 'K': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    def __init__(self,spec):
        '''
        takes in the cyclospectrum
        calculates the possible since amino acids the protein can have
        for use in expand function
        '''
        self.spectrum = []
        for sp in spec:
            self.spectrum.append(int(sp))
        self.counter = Counter(self.spectrum)
        self.singlePeptides = [] # Only possible single AA possible in spectrum
        for sp in self.spectrum:
            if sp > 186:
                break
            for peptide in self.masses:
                if sp == self.masses.get(peptide):
                    self.singlePeptides.append(peptide)

    def cyclopeptideSequencing(self):
        '''
        generates the cyclopeptide from the cyclospectrum
        uses branch and bound, can be exponential runtime
        returns a list of masses
        '''
        peptides = set(self.singlePeptides)
        cyclospec = []
        while len(peptides) != 0:
            peptides = self.expand(peptides)
            newPeptides = set()
            for i in range(len(peptides)):
                peptide = peptides.pop()
                mass = self.getMass(peptide)
                spec = self.cyclospectrum(peptide)
                if mass == self.spectrum[len(self.spectrum)-1] and spec == self.spectrum:
                    cyclospec.append(peptide)
                elif mass in self.spectrum: # elif self.consistent(spec):
                    newPeptides.add(peptide)
            peptides = newPeptides
        cyclicMasses = [] # Gets the weights of AA from the peptides
        for pep in set(cyclospec):
            weights = []
            for aa in pep:
                weights.append(self.masses.get(aa))
            cyclicMasses.append(weights)
        return cyclicMasses

    def consistent(self,spec):
        '''
        checks if the current spectrum is contained within the cyclospectrum
        DOESN'T work for some reason (From the textbook)
        '''
        c = Counter(spec)
        for sp in spec:
            if c.get(sp) > self.counter.get(sp,0):
                return False
        return True

    def cyclospectrum(self,seq):
        '''
        produces and returns cyclospectrum of the amino acid sequence
        '''
        cyclic = seq*2
        peptides = [seq]
        for i in range(len(seq)):
            for j in range(1,len(seq)):
                peptides.append(cyclic[i:i+j])
        spectrum = [0]
        for peptide in peptides:
            spectrum.append(self.getMass(peptide))
        return sorted(spectrum)

    def getMass(self,peptide):
        '''
        returns the mass of the peptide
        '''
        spec = 0
        for aa in peptide:
            spec += self.masses.get(aa)
        return spec

    def expand(self,peptides):
        '''
        branches and expands the peptides by appending
        possible single peptides that can be added onto the spectrum
        '''
        newPeptides = set()
        while len(peptides) != 0:
            peptide = peptides.pop()
            for branch in self.singlePeptides:
                newPeptides.add(peptide+branch)
        return newPeptides

def main():
    '''
    takes in from stdin the cyclospectrum
    creates the Peptide class and calculates the cyclopeptide masses
    outputs to stdout
    '''
    spec = sys.stdin.readlines()[0].rstrip()
    peptide = Peptide(spec.split())
    masses = peptide.cyclopeptideSequencing()
    aaString = []
    for mass in masses:
        aaString.append('-'.join(str(aa) for aa in mass))
    print(' '.join(mass for mass in aaString))

if __name__ == '__main__':
    main()

