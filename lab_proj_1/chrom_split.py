import file_output

in_base = "ceWS225"
in_ext = ".fa"
out_base = "chrom_"
out_ext = ".txt"

in_file = in_base + in_ext
fo = open(in_file, 'r')

for x in range(4):
	out_file = out_base + str(x) + out_ext
	file_out = open(out_file, 'w')

	while True:
		line = fo.readline()

		if line[0] == '>':
			file_out.close()
			break		
		else:
			file_out.write(line)

fo.close()
file_out.close()