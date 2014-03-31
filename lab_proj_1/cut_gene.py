poly_base = "poly_chr_"
poly_ext  = ".txt"
rflp_base = "rflp_names_"
rflp_ext  = ".txt"
out_base  = "tiny_chr_"
out_ext   = ".txt"
iteration = "3"

poly_file = poly_base + iteration + poly_ext
rflp_file = rflp_base + iteration + rflp_ext
out_file  = out_base  + iteration + out_ext

poly = open(poly_file, 'r')
outf = open(out_file, 'w')

for line in poly:
	line = line.split()

	rflp = open(rflp_file, 'r')

	for rf in rflp:
		rf = rf.split()

		if int(line[1]) == int(rf[1]):
			for i in range(len(line) - 1):
				outf.write(str(line[i]) + '\t')
			outf.write(str(line[len(line) - 1]) + '\n')

	rflp.close()

			

poly.close()
outf.close()