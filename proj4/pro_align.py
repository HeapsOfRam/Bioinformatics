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
			comp  = in_matrix[x - 1][y - 1] + sub_matrix[amino_hash[seq1[x]]][amino_hash[seq2[y]]]

			in_matrix[x][y] = max(comp, horiz, vert)

def traceback_gene(final_matrix):
	align_a = ""
	align_b = ""
	path = "" 
	tot_score = 0

	i = len(seq1) - 1
	j = len(seq2) - 1

	while i > 0 and j > 0:
		score = final_matrix[i][j]
		diag = final_matrix[i - 1][j - 1]
		horiz = final_matrix[i][j - 1]
		vert = final_matrix[i - 1][j]

		# print sub_matrix[amino_hash[seq1[i]]][amino_hash[seq2[j]]], i, j
		# print final_matrix[i][j]
		# print final_matrix[i - 1][j - 1]
		if score == diag + sub_matrix[amino_hash[seq1[i]]][amino_hash[seq2[j]]]:
			align_a = seq1[i] + align_a
			align_b = seq2[j] + align_b
			path = "D" + path
			i -= 1
			j -= 1
		elif score == vert + gap_score:
			align_a = seq1[i] + align_a
			align_b = "-" + align_b
			path = "V" + path	
			i -= 1
		elif score == horiz + gap_score:
			align_a = "-" + align_a
			align_b = seq2[j] + align_b
			path = "H" + path
			j -= 1
		# else:
		# 	print "You done did it"

		tot_score += final_matrix[i][j]

	while i > 0:
		align_a = seq1[i] + align_a
		align_b = align_b + "-"
		path = "V" + path
		i -= 1
		tot_score += final_matrix[i][j]
	while j > 0:
		align_a = align_a + "-"
		align_b = seq2[j] + align_b
		path = "H" + path
		j -= 1
		tot_score += final_matrix[i][j]

	align_a = seq1[0] + align_a
	align_b = seq2[0] + align_b

	return [align_a, align_b, path, tot_score]

file_list_a = ['input_1a.txt', 'input_2a.txt', 'input_3a.txt']
file_list_b = ['input_1b.txt', 'input_2b.txt', 'input_3b.txt']

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

	result_list = traceback_gene(score_matrix)

	alignment1 = result_list[0]
	alignment2 = result_list[1]
	alignment_path = result_list[2]
	final_score = result_list[3]

	print score_matrix

	print alignment1
	print alignment2
	print "PATH:", alignment_path
	print "SCORE:", final_score