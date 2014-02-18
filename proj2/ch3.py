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
	align_a = ""
	align_b = ""
	i = len(seq1) - 1
	j = len(seq2) - 1

	while i > 0 and j > 0:
		score = final_matrix[i][j]
		diag = final_matrix[i - 1][j - 1]
		vert = final_matrix[i][j - 1]
		horiz = final_matrix[i - 1][j]

		if score == diag + match_score or score == diag + mismatch_penalty:
			align_a = seq1[i] + align_a
			align_b = seq2[j] + align_b
			i -= 1
			j -= 1
		elif score == horiz + gap_penalty:
			align_a = seq1[i] + align_a
			align_b = "-" + align_b
			i -= 1
		elif score == vert + gap_penalty:
			align_a = "-" + align_a
			align_b = seq2[j] + align_b
			j -= 1
		else:
			print "You done did it"

	while i > 0:
		align_a = seq1[i] + align_a
		align_b = align_b + "-"
		i -= 1
	while j > 0:
		align_a = align_a + "-"
		align_b = seq2[j] + align_b
		j -= 1

	align_a = seq1[0] + align_a
	align_b = seq2[0] + align_b

	return [align_a, align_b]


# def traceback_gene(final_matrix):
# 	x = 1
# 	y = 1

# 	list_a = []
# 	list_b = []
# 	list_path = []

# 	non_zero = True
# 	x_over = False
# 	y_over = False
	
# 	while non_zero:
# 		if x > len(seq1):
# 			x = len(seq1) + 0
# 			x_over = True
# 		if y > len(seq2):
# 			y = len(seq2) + 0
# 			y_over = True

# 		x_spot = len(seq1) - x
# 		y_spot = len(seq2) - y

# 		val = final_matrix[x_spot][y_spot]
# 		diag = final_matrix[x_spot - 1][y_spot - 1]
# 		horiz = final_matrix[x_spot][y_spot - 1]
# 		vert = final_matrix[x_spot - 1][y_spot]

# 		print "X", x_spot, seq1[x_spot]
# 		print "Y", y_spot, seq2[y_spot]

# 		if val == diag + mismatch_penalty or val == diag + match_score:
# 			list_a.append(seq1[x_spot - 1])
# 			list_b.append(seq2[y_spot - 1])
# 			list_path.append('D')	
# 			# print "ALIST", list_a[x - 1]
# 			# print "BLIST", list_b[y - 1]
# 			x += 1
# 			y += 1
# 		else:
# 			if val == vert + gap_penalty:
# 				list_a.append(seq1[x_spot - 1])
# 				if y_over:
# 					list_b.insert(0, '-')
# 					list_path.insert(0, 'V')
# 				else:
# 					list_b.append('-')
# 					list_path.append('V')
# 				# print "ALIST", list_a[x - 1]
# 				# print "BLIST", list_b[y - 1]
# 				x += 1
# 			else:
# 				if val == horiz + gap_penalty:
# 					if x_over:
# 						list_a.insert(0, '-')
# 						list_path.insert(0, 'H')
# 					else:
# 						list_a.append('-')
# 						list_path.append('H')
# 					list_b.append(seq2[y_spot - 1])
# 					# print "ALIST", list_a[x - 1]
# 					# print "BLIST", list_b[y - 1]
# 					y += 1

# 		if len(seq1) <= x and len(seq2) <= y:
# 			if x_over:
# 				list_a.insert(0, '-')
# 				list_b.append(seq2[y_spot - 1])
# 				list_path.insert(0, 'H')
# 				print "XOVER Y", y_spot, seq2[y_spot - 1]
# 			else:
# 				if not x_over:
# 					list_a.append(seq1[x_spot])
# 			if y_over:
# 				list_a.append(seq1[x_spot - 1])
# 				#list_b.append(seq2[y_spot])
# 				list_b.insert(0, '-')
# 				list_path.insert(0, 'V')
# 				print "YOVER X", x_spot, seq1[x_spot - 1]
# 			else:
# 				if not y_over:
# 					list_b.append(seq2[y_spot])
# 			# print "ALIST", list_a[x_spot]
# 			# print "BLIST", list_b[y_spot]
# 			return [list_a, list_b, list_path]

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
	print result_list
	# result_list = traceback_gene(datmatrix, len(seq1) - 1, len(seq2) - 1)
	#print result_list
	#print len(result_list[0]), len(result_list[1]), len(result_list[2])
	
	# result_seq1 = ''.join(result_list[0][::-1])
	# result_seq2 = ''.join(result_list[1][::-1])
	# result_path = ''.join(result_list[2][::-1])

	# print result_seq1
	# print result_seq2
	# print "Path:", result_path

	matrix.gen_html_table(datmatrix, filename)
	# traceback_gene(datmatrix)

