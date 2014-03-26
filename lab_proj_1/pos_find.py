se_base   = 'start_end_'
se_ext    = '.txt'
chr_base  = 'split_chr_'
chr_ext   = '.txt'
out_base  = 'pos_poly_'
out_ext   = '.txt'
iteration = '2'

se_file  = se_base + iteration + se_ext
chr_file = chr_base + iteration + chr_ext
out_file = out_base + iteration + out_ext

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
		if num >= int(se[0]) and num <= int(se[1]):
			file_out.write(str(num) + '\t' + se[0] + '\t' + se[1] + '\n')

fo.close()
file_out.close()