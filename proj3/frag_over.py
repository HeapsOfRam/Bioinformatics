# GOAL: To determine the largest overlap between pairs of fragments
# INPUT: Set of fragments
# OUTPUT: The fragments, the resulting contig, and length of the overlapping region of each pair of fragments in the input file

import read_fasta
import file_output

frags_list = read_fasta.read_fasta_v1('assembly_out.txt')
frags = []

numFrags = 0
frags.append("")
for i in range(len(frags_list) - 1):
	if frags_list[i] == ',':
		numFrags += 1
		frags.append("")
	if frags_list[i] != ',' and frags_list[i] != '\'' and frags_list[i] != '[' and frags_list[i] != ']' and frags_list[i] != ' ':
		frags[numFrags] += frags_list[i]

file_output.file_open("fo_out.txt")

for i in range(numFrags - 1):
	for j in range(i + 1, numFrags):
		f1Len = len(frags[i])
		f2Len = len(frags[j])
		if f1Len < f2Len:
			minLen = f1Len
		else:
			minLen = f2Len
		overlap = 0
		frag1 = frags[i]
		frag2 = frags[j]
		k = minLen - 1
		while k >= 1 and overlap == 0:
			# compare suffix of frag1 to prefix of frag2
			if frag1[f1Len - k : f1Len] == frag2[0 : k]:
				# create contig
				contig = frag1[0 : f1Len - k] + frag2
				overlap = k
				print frag1, frag2, contig, overlap
				file_output.file_output([frag1, frag2, contig, overlap])
			elif frag2[f2Len - k : f2Len] == frag1[0 : k]:
				contig = frag2[0 : f2Len - k] + frag1
				overlap = k
				print frag1, frag2, contig, overlap
				file_output.file_output([frag1, frag2, contig, overlap])
			k -= 1

print frags
file_output.file_output(frags)
file_output.file_close()