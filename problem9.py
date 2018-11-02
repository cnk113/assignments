#!/usr/bin/env python3
# Name: Chang Kim (cnkim)
# Group Members: None

import sys

def assemble(lis):
	'''
	assembles the string
	'''
    sequence = lis[0]
    lis.remove(sequence)
    for i in lis:
        sequence += i[-1]
    return sequence

def main():
	'''
	removes the new lines after turning into a list
	prints out the the assembled string
	'''
    seq = sys.stdin.readlines()
    new = []
    for s in seq:
       new.append(s.rstrip())
    print(assemble(new))

if __name__ == '__main__':
    main()
