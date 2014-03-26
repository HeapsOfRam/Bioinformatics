import file_output

in_base = "targ_genes"
in_ext = ".txt"
out_base = "tar_chrom_"
out_ext = ".txt"

in_file = in_base + in_ext
fo = open(in_file, 'r')

file_out = open('tar_chrom_3.txt', 'w')
chrom = "CHROMOSOME_III"

for line in fo:
	line = line.split()

	if line[1] == chrom:
		for c in line:
			file_out.write(c + '\t')
		file_out.write('\n')

file_out.close()


fo.close()
