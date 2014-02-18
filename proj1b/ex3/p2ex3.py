import read_fasta

def compare_string(str1, str2):
	misses = []
	#if len(str1) != len(str2):
	#	return False
	for i in range(0, len(str1)):
		if(str1[i] != str2[i]):
			misses.append(i)
	return misses

afiles = ['input_ch2_ex3_1a.txt','input_ch2_ex3_2a.txt', 'input_ch2_ex3_3a.txt', 
					'input_ch2_ex3_4a.txt', 'hbbgene_dna.txt', 'hbbgene_protein.txt']
bfiles = ['input_ch2_ex3_1b.txt', 'input_ch2_ex3_2b.txt','input_ch2_ex3_3b.txt', 
					'input_ch2_ex3_4b.txt', 'sicklecell_dna_modified.txt', 'sicklecell_protein.txt']

q = 0
for file_name in afiles:
	str1 = read_fasta.read_fasta_v2(file_name)
	str2 = read_fasta.read_fasta_v2(bfiles[q])

	result = compare_string(str1, str2)

	if type(result) == list:
		if len(result) == 0:
			print "Match!"
		else:
			for n in result:
				print "Mismatch at", n + 1
	else:
		print "Strings are different"

	print ''

	q += 1