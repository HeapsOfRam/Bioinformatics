import codon

def convert_to_rna(dna):
	return dna.replace('T', 'U')
def check_sequence(dna):
	return dna.count('A') + dna.count('C') + dna.count('G') + dna.count('T') == len(dna)

dna = raw_input("Enter DNA Strand: ")
dna = dna.upper()

if check_sequence(dna):
	rna = convert_to_rna(dna)

	codon_string = ""
	for i in range(0, len(dna) / 3):
		codon_string += codon.get_codon(rna[i * 3:(i * 3) + 3])

	print codon_string

