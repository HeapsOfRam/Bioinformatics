in_base = "var_chr_"
in_ext = ".txt"
out_base = "split_chr_"
out_ext = ".txt"

file_in = in_base + '3' + in_ext
file_out = out_base + '3' + out_ext

fo = open(file_in, 'r')
file_out = open(file_out, 'w')

for line in fo:
	line = line.split()

	if len(line) > 4:
		if line[4].strip() != '.':
			for c in line:
				file_out.write(c + '\t')
			file_out.write('\n')

fo.close()
file_out.close