import read_fasta

def split_string(strang, spl):
	n = 0
	result_string = ""
	for sec in strang:
		n += 1
		if n > spl:
			result_string += " "
			n = 1
		result_string += sec
	return result_string

def compare_string(large, small, misses):
	for q in range(0, len(large) - (len(small) + 3)):
		n = 0
		result_string = ""
		for y in range(0, len(small)):
			if(large[q + y + n] != small[y]):
				if n > 0:
					break
				n += misses
			result_string += large[q + y + n]
			if len(result_string) <= len(small) + misses and len(result_string) >= len(small):
				return large[q : q + y + n]

nm = read_fasta.read_fasta_v2('nm_nucleotides.txt')
s = read_fasta.read_fasta_v2('s_nucleotides.txt')
nm_a = read_fasta.read_fasta_v2('nm_aminos.txt')
s_a = read_fasta.read_fasta_v2('s_aminos.txt')

print "small :", split_string(s, 3)
# answer = compare_string(nm, s, 3)
print "answer:", split_string(compare_string(nm, s, 3), 3)

print "small amino :", split_string(s_a, 1)
print "answer amino:", split_string(compare_string(nm_a, s_a, 1), 1) 
