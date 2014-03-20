# Group: Ryan March, Anita Uche, Vincent Eaton
import read_fasta
import matrix
import math

def total_aligned_positions(seq1, seq2):
	return len(seq1) - (seq1.count('-') + seq2.count('-'))

def determine_q(seq1, seq2, i, j):
	count = 1

	for x in range(len(seq1)):
		if seq1[x] == i:
			if seq2[x] == j:
				count += 1
		if seq1[x] == j:
			if seq2[x] == i:
				count += 1

	return float(count) / float(aligned_pos)

def determine_p(seq1, seq2, p):
	count = 1

	for x in range(len(seq1)):
		if seq1[x] == p and seq2[x] != '-':
			count += 1

	for x in range(len(seq1)):
		if seq2[x] == p and seq1[x] != '-':
			count += 1

	return float(count) / float(32)

def determine_e(p1, p2):
	return 2 * p1 * p2

def determine_chance(q, e):
	return q / e

def determine_log(chance):
	return math.log(chance, 2)

seq1 = read_fasta.read_fasta_v2('sub_input_1a.txt')
seq2 = read_fasta.read_fasta_v2('sub_input_1b.txt')

aligned_pos = total_aligned_positions(seq1, seq2)

amino_list = []

for x in seq1:
	if x not in amino_list:
		amino_list.append(x)

for x in seq2:
	if x not in amino_list:
		amino_list.append(x)

