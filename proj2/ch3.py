# Group: Ryan March, Anita Uche, Jeanna Kramer, Vince Eaton
import matrix
import read_fasta

gap_penalty = -1
mismatch_penalty = 0
match_score = 1

def init_matrix(empty_matrix):
	empty_matrix[0][0] = 0
	for n in range(1, len(empty_matrix)):
		empty_matrix[n][0] = empty_matrix[n - 1][0] + gap_penalty
	for m in range(1, len(empty_matrix[0])):
		empty_matrix[0][m] = empty_matrix[0][m - 1] + gap_penalty
	return empty_matrix

def fill_matrix(initialized_matrix):
	for n in range(1, len(initialized_matrix)):
		for m in range(1, len(initialized_matrix[n])):
			diag_val = initialized_matrix[n - 1][m - 1] + check_diag(initialized_matrix, n, m)#initialized_matrix[n - 1][m - 1]
			max_val = diag_val
			horiz_val = initialized_matrix[n - 1][m] + gap_penalty
			if horiz_val > max_val:
				max_val = horiz_val
			vert_val = initialized_matrix[n][m - 1] + gap_penalty
			if vert_val > max_val:
				max_val = vert_val
			initialized_matrix[n][m] = max_val
	return initialized_matrix

def check_diag(initialized_matrix, n, m):
	if seq1[n - 1] == seq2[m - 1]:
		return match_score
	else:
		return mismatch_penalty

def gen_list(num):
	return [None for c in range(num)]

def traceback_gene(final_matrix):
	align_a = ""
	align_b = ""
	path = "" 

	i = len(seq1) - 1
	j = len(seq2) - 1

	while i > 0 and j > 0:
		score = final_matrix[i][j]
		diag = final_matrix[i - 1][j - 1]
		horiz = final_matrix[i][j - 1]
		vert = final_matrix[i - 1][j]

		if score == diag + match_score or score == diag + mismatch_penalty:
			align_a = seq1[i] + align_a
			align_b = seq2[j] + align_b
			path = "D" + path
			i -= 1
			j -= 1
		elif score == vert + gap_penalty:
			align_a = seq1[i] + align_a
			align_b = "-" + align_b
			path = "V" + path	
			i -= 1
		elif score == horiz + gap_penalty:
			align_a = "-" + align_a
			align_b = seq2[j] + align_b
			path = "H" + path
			j -= 1
		else:
			print "You done did it"

	while i > 0:
		align_a = seq1[i] + align_a
		align_b = align_b + "-"
		path = "V" + path
		i -= 1
	while j > 0:
		align_a = align_a + "-"
		align_b = seq2[j] + align_b
		path = "H" + path
		j -= 1

	align_a = seq1[0] + align_a
	align_b = seq2[0] + align_b

	return [align_a, align_b, path]

def find_matches(str1, str2):
	matches = 0
	for i in range(0, len(str1)):
		if str1[i] == str2[i]:
			matches += 1
	return matches

def find_mismatches(str1, str2):
	mismatches = 0
	for i in range(0, len(str1)):
		if str1[i] != '-' and str2[i] != '-':
			if str1[i] != str2[i]:
				mismatches += 1
	return mismatches

def find_gaps(str1, str2):
	gaps = 0
	for i in range(0, len(str1)):
		if str1[i] == '-' or str2[i] == '-':
			gaps += 1
	return gaps

def match_percentage(str1, str2):
	n_match = find_matches(str1, str2)
	return float(n_match) * 100 / float(len(str1))

filename1 = 'input_ch3_1a.txt'
filename2 = 'input_ch3_1b.txt'

file_lista = ['input_ch3_1a.txt', 'input_ch3_2a.txt']
file_listb = ['input_ch3_1b.txt', 'input_ch3_2b.txt']

for x in range(len(file_lista)):
	print ""

	filename = "table" + str(x + 1) + '.html'
	filename1 = file_lista[x]
	filename2 = file_listb[x]
	
	seq1 = read_fasta.read_fasta_v1(filename1)
	seq2 = read_fasta.read_fasta_v1(filename2)

	datmatrix = matrix.gen_matrix(len(seq1) + 1, len(seq2) + 1)

	datmatrix = init_matrix(datmatrix)
	datmatrix = fill_matrix(datmatrix)

	print datmatrix

	result_list = traceback_gene(datmatrix)

	alignment1 = result_list[0]
	alignment2 = result_list[1]
	alignment_path = result_list[2]

	num_matches = find_matches(alignment1, alignment2)
	num_mismatches = find_mismatches(alignment1, alignment2)
	num_gaps = find_gaps(alignment1, alignment2)

	print "Path:", alignment_path
	print "Matches:", num_matches, "Mismatches:", num_mismatches, "Gaps:", num_gaps
	print "Match percent:", match_percentage(alignment1, alignment2)
	print "Aligned Sequences:"
	print alignment1
	print alignment2

	matrix.gen_html_table(datmatrix, filename)