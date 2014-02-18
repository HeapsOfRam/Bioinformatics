def convert_to_rna(dna):
	return dna.replace('T', 'U')
def check_sequence(dna):
	return dna.count('A') + dna.count('C') + dna.count('G') + dna.count('T') == len(dna)

done = False
while done == False:
	dna = raw_input("Input DNA Sequence (DONE to quit): ")

	dna = dna.upper()

	if dna == "DONE":
		done = True
	else:
		if check_sequence(dna):
			rna = convert_to_rna(dna)
			print rna
		else:
			print "Invalid sequence, please try again"