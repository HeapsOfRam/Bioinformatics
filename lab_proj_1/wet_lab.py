import read_fasta

file_in_base = "split_chr_"
file_in_ext = ".txt"
file_out_base = "poly_chr_"
file_out_ext = ".txt"
iteration = "2"

file_in = file_in_base + iteration + file_in_ext
file_oname = file_out_base + iteration + file_out_ext

fo = open(file_in, 'r')
file_out = open(file_oname, 'w')

for line in fo:
	line = line.split('\t')
	if(len(line) >= 4):
		num = int(line[1])

		if line[4].strip() != '.':
			for i in range(len(line) - 1):
				file_out.write(str(line[i]) + '\t')
			file_out.write(str(line[len(line) - 1]))
			# file_out.write('\n')

fo.close()
file_out.close()