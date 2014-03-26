import file_output

in_base_1 = "HwVarChrII"
in_base_2 = "HwVarChrIII"
in_ext = ".vcf"
out_base_1 = "var_chr_2"
out_base_2 = "var_chr_3"
out_ext = ".txt"

in_file = in_base_1 + in_ext
fo = open(in_file, 'r')

out_file = out_base_1 + out_ext
file_out = open(out_file, 'w')

c = 'a'
tabs = 0

while c:
	c = fo.read(1)

	if c == '\t':
		tabs += 1

	if tabs >= 9:
		tabs = 0
		file_out.write('\n')
	else:
		file_out.write(c)

fo.close()
file_out.close()

print "File 1 Done"

# DOING AGAIN NOT DRY

in_file = in_base_2 + in_ext
fo = open(in_file, 'r')

out_file = out_base_2 + out_ext
file_out = open(out_file, 'w')

c = 'a'

while c:
	c = fo.read(1)

	if c == '\t':
		tabs += 1

	if tabs >= 9:
		tabs = 0
		file_out.write('\n')
	else:
		file_out.write(c)

fo.close()
file_out.close()

print "File 2 Done"


# line = fo.readline()
# fo.close()

# tabs = 0

# for i in range(len(line)):
# 	c = line[i]

# 	if c == '\t':
# 		tabs += 1

# 	if tabs >= 9:
# 		line[i] = '\n'
# 		tabs = 0

# for c in line:
# 	if c == '\t':
# 		tabs += 1

# 	if tabs >= 9:
# 		c = '\n'
# 		tabs = 0

# 	print c

