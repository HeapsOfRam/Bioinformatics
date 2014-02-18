import read_fasta

files = ['input_ch2_ex3_1a.txt', 'input_ch2_ex3_1b.txt', 'input_ch2_ex3_2a.txt',
					'input_ch2_ex3_2b.txt','input_ch2_ex3_3a.txt', 'input_ch2_ex3_3b.txt', 
					'input_ch2_ex3_4a.txt', 'input_ch2_ex3_4b.txt', 'hbbgene_dna.txt',
					'sicklecell_dna_modified.txt', 'hbbgene_protein.txt', 'sickecell_protein.txt']
afiles = ['input_ch2_ex3_1a.txt','input_ch2_ex3_2a.txt', 'input_ch2_ex3_3a.txt', 
					'input_ch2_ex3_4a.txt', 'hbbgene_dna.txt', 'hbbgene_protein.txt']
bfiles = ['input_ch2_ex3_1b.txt', 'input_ch2_ex3_2b.txt','input_ch2_ex3_3b.txt', 
					'input_ch2_ex3_4b.txt', 'sicklecell_dna_modified.txt', 'sickecell_protein.txt']

for i in(0, len(afiles)):
	str1 = read_fasta.read_fasta_v2(afiles[i])
	str2 = read_fasta.read_fasta_v2(bfiles[i])

	if str1 is str2:
		print "Match!"
	else:
		print "Mismatch!"
