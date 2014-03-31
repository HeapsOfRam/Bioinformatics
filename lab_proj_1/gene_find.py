import read_fasta

def chrom_len(check):
	check = check.lower()
	return check.count('a') + check.count('t') + check.count('c') + check.count('g')

# def poly_det(small, large, place, pol):
# 	l = 0
# 	s = 0
# 	count = 0
# 	match = True
# 	pol = False

# 	while l < len(large):
# 		l = count
# 		s = 0
# 		match = True
# 		pol = False
# 		while s < len(small) and match:
# 			if small[s] != large[l]:
# 				if small[s] == chromosome[place]:
# 					if pol != large[l]:
# 						match = False
# 						pol = True

# 			s += 1
# 			l += 1

# 		if match:
# 			return [pol, large[count : l]]

# 		count += 1

# 	return [False, False]

rebase_base = "rebases"
rebase_ext  = ".txt"
chrom_base  = "chrom_full_"
chrom_ext   = ".txt"
tiny_base   = "tiny_chr_"
tiny_ext    = ".txt"
out_base    = "final_ans_"
out_ext     = ".txt"
iteration   = "3"

rebase_file = rebase_base + rebase_ext
chrom_file  = chrom_base + iteration + chrom_ext
tiny_file   = tiny_base + iteration + tiny_ext
out_file    = out_base + iteration + out_ext

cf = open(chrom_file, 'r')
tf = open(tiny_file, 'r')
of = open(out_file, 'w')

chromosome = cf.readline()
cf.close()

rf = open(rebase_file, 'r')
rebase_dictionary = {}
for reb in rf:
	reb = reb.split()
	if len(reb[1]) == chrom_len(reb[1]):
		rebase_dictionary[reb[1]] = reb[0]
rf.close()

for tiny in tf:
	tiny = tiny.split()
	loc = int(tiny[1])

	for reb in rebase_dictionary:
		low_bound = loc - len(reb)
		high_bound = loc + len(reb)

		if low_bound < 0 :
			low_bound = 0
		if high_bound >= len(chromosome):
			high_bound = len(chromosome) - 1

		rebase_check = reb.lower()
		chrom_check = chromosome[low_bound : high_bound].lower()


		if rebase_check in chrom_check:
			of.write(rebase_dictionary[reb] + '\t' + str(loc) + '\t' + "Create" +  "\n")

		chrom_check = list(chromosome)
		chrom_check[loc] = tiny[4]
		chrom_check = "".join(chrom_check)
		chrom_check = chrom_check[low_bound : high_bound]
		chrom_check = chrom_check.lower()

		if rebase_check in chrom_check:
			of.write(rebase_dictionary[reb] + '\t' + str(loc) + '\t' + "Destroy" + '\n')


		# result = poly_det(reb[1], chromosome[low_bound : high_bound], loc, tiny[4])

		# if result[0] == False:
		# 	strain = "Destroy"
		# else:
		# 	strain = "Create"

		# if result[0] != False:
		# 	of.write(reb[0], loc, strain)

of.close()
tf.close()
