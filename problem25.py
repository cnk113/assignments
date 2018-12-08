#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys
from itertools import permutations

'''
'''
class Spectrum:
    '''
    '''
    masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
    def __init__(self):
        '''
        '''
        self.spectrum = [0]

    def combinations(self,seq):
        '''
        '''
        perms = [''.join(permutations(seq[i:])) for i in range(len(seq))]
        for perm in perms:
            if perm not in self.peptides:
                self.peptides[perm] = 0
            mass = 0
            for peptide in perm:
                mass += masses.get(peptide)
            self.spectrum.append(mass)
        return sorted(self.spectrum)


def main():
    '''
    '''
    protein = sys.stdin.readlines()
    spec = Spectrum()
    peptides = spec.combinations(protein.rstrip())
    print('0 ' + ' '.join(m) for m in peptides) 

if __name__ == "__main__":
    main()
