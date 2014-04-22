# 1. READ IN INPUT
# 2. SET READING POSITION AT FIRST NUCLEOTIDE (READING FRAME 1 - NUCLEOTIDE 0)
# 3. BEGINNING AT THE STARTING POSITION, SEARCH IN TRIPLETS FOR AUG. IF FOUND, JUMP TO STEP 5. 
# 	OTHERWISE, GO TO STEP 
# 4. INCREMENT THE STARTING POSITION BY 1 (NEXT READING FRAME) IF THE STARTING POSITION IS
#	< 3 , GO BACK TO STEP 3. OTHERWISE, YOU HAVE NOT FOUND AN ORF. PRINT NOT FOUND
# 5. ONCE YOU HAVE FOUND A START CODON, SEARCH IN TRIPLETS WITH THE SAME READING FRAME AND LOOK
#	FOR A STOP CODON. IF A STOP CODON IS FOUND AND THE LENGTH IS >= 60, YOU HAVE FOUND ACCEPTABLE
#	ORF. PRINT RESULTS. IF STOP CODON NOT FOUND, RETURN TO STEP 4

def orf_check(dna_strand):
	global orf_found

	orf_length = 0
	orf = ""

	for i in range (0, len(dna_strand), 3):
		orf_length += 3

		if dna_strand[i:i + 3].upper() in stop_codons and orf_length >= minimum_length:
			orf_found = True
			orf += dna_strand[i: i + 3]
			print "ORF FOUND in " + in_file_base + str(iteration)
			out_file.write(orf)
			out_file.close()

		orf += dna_strand[i:i + 3] + "-"

start_codon = "AUG"
stop_codons = ["UAA", "UAG", "UGA"]
minimum_length = 60

in_file_base = "strand_"
in_file_ext = ".txt"
out_file_base = "result_"
out_file_ext = ".txt"

for iteration in range(1, 6):
	in_file = open(in_file_base + str(iteration) + in_file_ext, 'r')
	out_file = open(out_file_base + str(iteration) + out_file_ext, 'w')
	orf_found = False

	in_file.readline()

	strand = in_file.readline()
	reverse_strand = strand[::-1]

	for x in range(3):
		#print str(orf_found) + str(iteration) + '1'

		if orf_found != True:
			if strand[x:x + 3].upper() == start_codon:
				orf_check(strand[x:])

		#print str(orf_found) + str(iteration) + '2'

		if orf_found != True:
			if reverse_strand[x:x + 3].upper() == start_codon:
				orf_check(reverse_strand[x:])

		#print str(orf_found) + str(iteration) + '3'	


	in_file.close()

	if orf_found != True:
		print "No ORF Found in " + in_file_base + str(iteration)
		out_file.write("None")
		out_file.close()