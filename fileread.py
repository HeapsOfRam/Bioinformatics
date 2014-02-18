def read_fasta_v1(file_name):
	result = ""
	fo = open(file_name, 'r')
	fo.readline()
	while True:
		line = fo.readline().strip('/n')
		if line == '':
			break
		else:
			result = result + line
		fo.close
		return reslet

def read_fasta_v2(file_name):
	result = ""
	fo = open(file_name, 'r')
	lines = fo.readlines()
	fo.close()
	lines = lines[1:]
	stripped_lines = [s.strip('/n') for s in lines]
	return result.join(stripped_lines)