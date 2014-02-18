def convert_to_rna(dna):
	return dna.replace('T', 'U')

def gc(dna):
	return (dna.count('G') + dna.count('C')) * 100 / len(dna)

dna = raw_input("Input DNA Sequence: ")

rna = convert_to_rna(dna)
gcPercent = gc(dna)

print rna
print gcPercent