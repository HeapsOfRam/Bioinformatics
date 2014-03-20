# Group: Ryan March, Anita Uche, Vincent Eaton
import read_matrix
import read_fasta

def dictionarize(to_be):
	dic = {}
	for x in range(len(to_be) - 1):
		dic.update({to_be[x] : x})
	return dic

file_list_a = ['input_1a.txt']
file_list_b = ['input_1b.txt']

inp = read_matrix.read_matrix("amino_matrix.txt")

sub_seq = inp[0]
sub_matrix = inp[1]

aminohash = dictionarize(sub_seq)

for x in range(len(file_list_a) - 1):
	seq1 = read_fasta.read_fasta_v2(file_list_a[x])
	seq2 = read_fasta.read_fasta_v2(file_list_b[x])

print sub_matrix