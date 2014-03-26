import file_output

in_base = "tar_chrom_"
in_ext = ".txt"
out_base = "start_end_"
out_ext = ".txt"

in_file = in_base + '3' + in_ext
fo = open(in_file, 'r')

file_out = open(out_base + '3' + out_ext, 'w')

for line in fo:
	line = line.split()

	file_out.write(line[2] + '\t' + line[3] + '\n')


file_out.close()


fo.close()
