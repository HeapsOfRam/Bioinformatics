def replace_t(dna):
	return dna.replace('T', 'U')
def replace_a(dna):
	return dna.replace('A', 'Y')
def replace_c(dna):
	return dna.replace('C', 'I')
def replace_g(dna):
	return dna.replace('G', 'O')
def return_t(dna):
	return dna.replace('Y', 'T')
def return_a(dna):
	return dna.replace('U', 'A')
def return_c(dna):
	return dna.replace('O', 'C')
def return_g(dna):
	return dna.replace('I', 'G')
def complement_dna(dna):
	inter_dna = replace_t(dna)
	inter_dna = replace_a(inter_dna)
	inter_dna = replace_g(inter_dna)
	inter_dna = replace_c(inter_dna)
	inter_dna = return_t(inter_dna)
	inter_dna = return_a(inter_dna)
	inter_dna = return_g(inter_dna)
	return return_c(inter_dna)
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
			comp_dna = complement_dna(dna)
			print comp_dna
		else:
			print "Invalid sequence, please try again"