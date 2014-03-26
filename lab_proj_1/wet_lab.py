import read_fasta

file_in_base = "var_chr_"
file_in_ext = ".txt"

file_in = file_in_base + "3" + file_in_ext

fo = open(file_in, 'r')
file_out = open("poly_chr_3.txt", 'w')

for line in fo:
	line = line.split('\t')
	if(len(line) >= 4):
		num = int(line[1])

		if line[4].strip() != '.':
			file_out.write(str(line) + '\n')

fo.close()
file_out.close()