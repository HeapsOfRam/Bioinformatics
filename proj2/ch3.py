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

# def traceback_gene(final_matrix):
# 	list_a = []
# 	list_b = []
# 	x_over = False
# 	y_over = False
# 	for y in range(0, len(final_matrix)):
# 		for x in range(0, len(final_matrix[y])):
# 			x_spot = len(seq1) - x
# 			y_spot = len(seq2) - y
# 			val = final_matrix[x_spot][y_spot]
# 			diag = final_matrix[x_spot - 1][y_spot - 1]
# 			horiz = final_matrix[x_spot - 1][y_spot]
# 			vert = fill_matrix[x_spot][y_spot - 1]
# 			if val == diag + mismatch_penalty or val == diag + match_score:
# 				list_a.append(seq1[x_spot])
# 				list_b.append(seq2[y_spot])
# 			else:
# 				if val == horiz + gap_penalty:
# 					list_a.append(seq1[x_spot])


def traceback_gene(final_matrix):
	x = 1
	y = 1
	list_a = []
	list_b = []
	non_zero = True
	x_over = False
	y_over = False
	while non_zero:
		if x >= len(seq1):
			x = len(seq1) + 0
			x_over = True
		if y >= len(seq2):
			y = len(seq2) + 0
			y_over = True
		x_spot = len(seq1) - x
		y_spot = len(seq2) - y
		val = final_matrix[x_spot][y_spot]
		diag = final_matrix[x_spot - 1][y_spot - 1]
		horiz = final_matrix[x_spot - 1][y_spot]
		vert = final_matrix[x_spot][y_spot - 1]
		if val == diag + mismatch_penalty or val == diag + match_score:
			list_a.append(seq1[x_spot])
			list_b.append(seq2[y_spot])
			x += 1
			y += 1
		else:
			if val == horiz + gap_penalty:
				list_a.append(seq1[x_spot])
				if y_over:
					list_b.insert(0, '-')
				else:
					list_b.append('-')
				x += 1
			else:
				if val == vert + gap_penalty:
					if x_over:
						list_a.insert(0, '-')
					else:
						list_a.append('-')
					list_b.append(seq2[y_spot])
					y += 1

		if len(seq1) <= x and len(seq2) <= y:
			if x_over:
				list_a.insert(0, '-')
				list_b.append(seq2[y_spot])
			if y_over:
				list_a.append(seq1[x_spot])
				list_b.insert(0, '-')
			return [list_a, list_b]

# def traceback_gene(final_matrix, x, y):
# 	list_a = []
# 	list_b = []
# 	non_zero = True
# 	while non_zero:
# 		if y < 0:
# 			y = 0
# 		if x < 0:
# 			x = 0
# 		if x == 0 and y == 0:
# 			non_zero = False
# 		print "X", x
# 		print "Y", y
# 		diag = final_matrix[x - 1][y - 1]
# 		horiz = final_matrix[x - 1][y]
# 		vert = final_matrix[x][y - 1]
# 		val = final_matrix[x][y]
# 		if val == diag + mismatch_penalty or val == diag + match_score:
# 			list_a.append(seq1[x])
# 			list_b.append(seq2[y])
# 			x -= 1
# 			y -= 1
# 		else:
# 			if val == horiz + gap_penalty:
# 				list_a.append(seq1[x])
# 				list_b.append('-')
# 				x -= 1
# 			else:
# 				if val == vert + gap_penalty:
# 					list_a.append('-')
# 					list_b.append(seq2[y])
# 					y -= 1
# 	return [list_a, list_b]

filename1 = 'input_ch3_1a.txt'
filename2 = 'input_ch3_1b.txt'

file_lista = ['input_ch3_1a.txt', 'input_ch3_2a.txt']
file_listb = ['input_ch3_1b.txt', 'input_ch3_2b.txt']

for x in range(len(file_lista)):
	num_gaps = 0
	
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
	# result_list = traceback_gene(datmatrix, len(seq1) - 1, len(seq2) - 1)
	print result_list
	print len(result_list[0]), len(result_list[1])
	matrix.gen_html_table(datmatrix, filename)
	# traceback_gene(datmatrix)

