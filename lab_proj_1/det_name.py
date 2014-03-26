tar_base = 'tar_chrom_'
tar_ext = '.txt'
pos_base = 'pos_poly_'
pos_ext = '.txt'
out_base = 'rflp_names_'
out_ext = '.txt'
iteration = '3'

tar_file = tar_base + iteration + tar_ext
pos_file = pos_base + iteration + pos_ext
out_file = out_base + iteration + out_ext

tf = open(tar_file, 'r')
pf = open(pos_file, 'r')
file_out = open(out_file, 'w')

for target in tf:
	target = target.split()
	for pos in pf:
		pos = pos.split()
		if pos[0] >= target[2] and pos[0] <= target[3]:
			print pos[0], target[2], target[3]
			file_out.write(target[0] + '\t' + pos[0] + '\n')

tf.close()
pf.close()
file_out.close()