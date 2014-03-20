# Group: Ryan March, Anita Uche, Vincent Eaton
import read_matrix
import read_fasta
import matrix

def dictionarize(to_be):
	dic = {}
	for x in range(len(to_be)):
		dic.update({to_be[x] : x})
	return dic

def init_matrix(in_matrix):
	in_matrix[0][0] = 0
	for x in range(1, len(in_matrix)):
		in_matrix[x][0] = in_matrix[x - 1][0] + gap_score
	for x in range(1, len(in_matrix[0])):
		in_matrix[0][x] = in_matrix[0][x - 1] + gap_score

def fill_matrix(in_matrix, seq1, seq2):
	for x in range(1, len(seq1)):
		for y in range(1, len(seq2)):
			horiz = in_matrix[x][y - 1] + gap_score
			vert  = in_matrix[x - 1][y] + gap_score
			comp  = sub_matrix[amino_hash[seq1[x]]][amino_hash[seq2[y]]]

			in_matrix[x][y] = max(comp, horiz, vert)

file_list_a = ['input_1a.txt']
file_list_b = ['input_1b.txt']

gap_score = -1

inp = read_matrix.read_matrix("amino_matrix.txt")

sub_seq = inp[0]
sub_matrix = inp[1]

amino_hash = dictionarize(sub_seq)

for x in range(len(file_list_a)):
	seq1 = read_fasta.read_fasta_v2(file_list_a[x])
	seq2 = read_fasta.read_fasta_v2(file_list_b[x])

	score_matrix = matrix.gen_matrix(len(seq1), len(seq2))

	init_matrix(score_matrix)

	fill_matrix(score_matrix, seq1, seq2)
	print score_matrix
