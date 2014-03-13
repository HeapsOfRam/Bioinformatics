import read_fasta
import matrix

def compare(frag1, frag2):
	f1Len = len(frag1)
	f2Len = len(frag2)
	k = f1Len
	overlap = 0

	while k >= 1 and overlap == 0:
		# compare suffix of frag1 to prefix of frag2
		if frag1[f1Len - k : f1Len] == frag2[0 : k]:
			# create contig
			contig = frag1[0 : f1Len - k] + frag2
			overlap = k
		k -= 1

	return overlap


def combine(frag1, frag2, overlap):
	frag1 += frag2[overlap : ]
	return frag1

def find_max(mat):
	max_x = 0
	max_y = 0

	for row in range(len(mat)):
		for col in range(len(mat[row])):
			if mat[row][col] > mat[max_x][max_y]:
				max_x = row
				max_y = col

	return [max_x, max_y]


file_base = "assembly_out_"
file_ext = ".txt"

file_list = []

for i in range(1, 6):
	file_list.append(file_base + str(i) + file_ext)

for fname in file_list:
	frags_list = read_fasta.read_fasta_v1(fname)
	fragments = []

	numFrags = 0
	fragments.append("")
	for i in range(len(frags_list) - 1):
		if frags_list[i] == ',':
			numFrags += 1
			fragments.append("")
		if frags_list[i] != ',' and frags_list[i] != '\'' and frags_list[i] != '[' and frags_list[i] != ']' and frags_list[i] != ' ':
			fragments[numFrags] += frags_list[i]

	while len(fragments) > 1:
		dat_matrix = matrix.gen_matrix(len(fragments), len(fragments))

		for row in range(len(dat_matrix)):
			for col in range(len(dat_matrix[row])):
				if row == col:
					dat_matrix[row][col] = -1
				else:
					dat_matrix[row][col] = compare(fragments[row], fragments[col])

		coords = find_max(dat_matrix)
		row = coords[0]
		col = coords[1]

		fragments.append(combine(fragments[row], fragments[col], dat_matrix[row][col]))

		for c in range(len(dat_matrix[row])):
			dat_matrix[row][c] = -1
		for r in range(len(dat_matrix)):
			dat_matrix[r][col] = -1

		remove_row = fragments[row]
		remove_col = fragments[col]
		fragments.remove(remove_row)
		fragments.remove(remove_col)

	print fragments