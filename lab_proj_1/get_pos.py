#!/usr/bin/python

start_end = []
f2 = open('start_end')
for a in f2:
	sp = a.split(' ')
	start_end.append((sp[0].strip(), sp[1].strip()))
f2.close()

f = open('newvar.txt', 'r')
for line in f: 
	line = line.split('\t')
	num = int(line[1])
	for se in start_end:
		if num >= int(se[0]) and num <= int(se[1]):
			if line[4].strip() != '.':
				print(se)
				print(line)

f.close()
