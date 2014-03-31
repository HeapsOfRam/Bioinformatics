in_base = "chrom_"
in_ext = ".txt"
out_base = "chrom_full_"
out_ext = ".txt"
iteration = "3"

in_file = in_base + iteration + in_ext
out_file = out_base + iteration + out_ext

file_in = open(in_file, 'r')
file_out = open(out_file, 'w')

file_in.readline()

for line in file_in:
	file_out.write(line.strip())

file_in.close()
file_out.close()