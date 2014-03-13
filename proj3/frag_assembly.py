# GROUP: Ryan March, Vince Eaton, Anita Uche
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

fMin = 5
fMax = 10
fold = 5

file_base = 'fa_input_'
file_ext = '.txt'
output_base = 'assembly_out_'

file_list = []

for i in range(1, 5):
	file_list.append(file_base + str(i) + file_ext)

num = 1

for fname in file_list:
	seq = read_fasta.read_fasta_v1(fname)

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
	print numFrags

	for i in range(len(coverage) - 1):
		print coverage[i]

	file_output.file_write(output_base + str(num) + file_ext, frags)
	num += 1