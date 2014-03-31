se_base   = 'start_end_'
se_ext    = '.txt'
chr_base  = 'split_chr_'
chr_ext   = '.txt'
out_base  = 'pos_poly_'
out_ext   = '.txt'
iteration = '3'

se_file  = se_base  + iteration + se_ext
chr_file = chr_base + iteration + chr_ext
out_file = out_base + iteration + out_ext

offset = 100000

start_end = []
fstart = open(se_file, 'r')
for a in fstart:
	sp = a.split()
	start_end.append((sp[0].strip(), sp[1].strip()))
fstart.close()

fo = open(chr_file, 'r')
file_out = open(out_file, 'w')

for line in fo:
	line = line.split()
	num = int(line[1])
	
	for se in start_end:
		low_bound = int(se[0]) - offset
		high_bound = int(se[1]) + offset

		if num >= low_bound and num <= high_bound:
			file_out.write(str(num) + '\t' + str(low_bound) + '\t' + str(high_bound) + '\n')

fo.close()
file_out.close()