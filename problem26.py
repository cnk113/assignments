#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

class Peptide:
    '''
    '''
    masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'N': 114,'D': 115, 'K': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    def __init__(self,spec):
        '''
        '''
        self.spectrum = []
        for sp in spec:
            self.spectrum.append(int(sp))
        self.singlePeptides = []
        for sp in self.spectrum:
            if sp > 186:
                break
            for peptide in self.masses:
                if sp == self.masses.get(peptide):
                    self.singlePeptides.append(peptide)

    def cyclopeptideSequencing(self):
        '''
        '''
        peptides = self.singlePeptides.copy()
        cyclospec = []
        while len(peptides) != 0:
            peptides = self.expand(peptides)
            newPeptides = []
            for i in range(len(peptides)):
                peptide = peptides.pop()
                mass = self.getMass(peptide)
                spec = self.cyclospectrum(peptide)
                if mass == self.spectrum[len(self.spectrum)-1] and spec == self.spectrum:
                    cyclospec.append(peptide)
                elif self.consistent(spec):
                    newPeptides.append(peptide)
            peptides = newPeptides
        cyclicMasses = []
        for pep in cyclospec:
            weights = []
            for aa in pep:
                weights.append(self.masses.get(aa))
            cyclicMasses.append(weights)
        return cyclicMasses
    
    def consistent(self,spec):
        '''
        '''
        for sp in spec:
            if spec.count(sp) > self.spectrum.count(sp):
                return False
        return True

    def cyclospectrum(self,seq):
        '''
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
        '''
        spec = 0
        for aa in peptide:
            spec += self.masses.get(aa)
        return spec

    def expand(self,peptides):
        '''
        '''
        newPeptides = []
        while len(peptides) != 0:
            peptide = peptides.pop()
            for branch in self.singlePeptides:
                newPeptides.append(peptide+branch)
        return newPeptides

def main():
    '''
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

