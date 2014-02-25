# GOAL: To generate random fragments from an input sequence
# INPUT: A single nucleotide sequence, user-defined minimum fragment size, maximum fragment size and coverage fold
# OUTPUT: A set of fragments
# NOTE: Substring is assumed exclusive, thus substring(1,4) includes positions 1,2,3 only

import random
import read_fasta
import file_output

def coverageMet(coverage, fold):
	for i in range(0, len(coverage)):
		if coverage[i] < fold:
			return False
	return True

# seq  = raw_input("enter your input: ")
# fMin = raw_input("enter minimum fragment size: ")
# fMax = raw_input("enter maximum fragment size: ")
# fold = raw_input("input coverage fold expected: ")

seq = read_fasta.read_fasta_v1('fa_input_1.txt')
fMin = 5
fMax = 10
fold = 5

coverage = []

for i in range(0, len(seq) - 1):
	coverage.append(0)

numFrags = 0
frags = []

while not(coverageMet(coverage, fold)):
	randLength = random.randint(int(fMin), int(fMax) + 1)
	randStart  = random.randint(0, len(seq) - randLength)
	frags.append(seq[randStart:randStart + randLength])
	numFrags += 1

	# update coverage
	for i in range(randStart, randStart + (randLength - 1)):
		coverage[i] += 1

print frags

file_output.file_write("assembly_out.txt", frags)