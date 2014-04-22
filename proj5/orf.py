# Ryan March, Vincent Eaton, Anita Uche

def orf_check(dna_strand):
	global orf_count

	orf_length = 0
	orf = ""
	base_orf = ""

	for i in range (0, len(dna_strand), 3):
		orf_length += 3

		if dna_strand[i:i + 3].upper() in stop_codons and orf_length >= minimum_length:
			orf_count += 1
			orf += dna_strand[i:i + 3]
			base_orf = dna_strand[i:i + 3]
			print "ORF FOUND in " + in_file_base + str(iteration)
			out_file.write(orf.upper() + '\n')
			return [True, orf]

		orf += dna_strand[i:i + 3] + "-"
		base_orf += dna_strand[i:i + 3]

	return [False, orf]

start_codons = ["AUG", "ATG"]
stop_codons = ["UAA", "TAA", "UAG", "TAG", "UGA", "TGA"]
minimum_length = 60

in_file_base = "strand_"
in_file_ext = ".txt"
out_file_base = "result_"
out_file_ext = ".txt"

for iteration in range(1, 7):
	in_file = open(in_file_base + str(iteration) + in_file_ext, 'r')
	out_file = open(out_file_base + str(iteration) + out_file_ext, 'w')
	orf_count = 0
	covered = False

	in_file.readline()

	strand = in_file.readline()
	reverse_strand = strand[::-1]

	for x in range(len(strand) - 4):
		if strand[x:x + 3].upper() in start_codons:
			results = orf_check(strand[x:])

		covered = results[0]

		if covered:
			x += len(results[1])
			covered = False

		if reverse_strand[x:x + 3].upper() in start_codons:
			results = orf_check(reverse_strand[x:])

		covered = results[0]

		if covered:
			x += len(results[1])
			covered = False

	in_file.close()

	if orf_count == 0:
		print "No ORF Found in " + in_file_base + str(iteration)
		out_file.write("None")
	
	out_file.close()
