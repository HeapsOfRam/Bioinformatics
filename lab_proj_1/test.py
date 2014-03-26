#!/usr/bin/python

start_end = []
f2 = open('start_end')
for a in f2:
	sp = a.split(' ')
	start_end.append((sp[0].strip(), sp[1].strip()))
f2.close()
print(start_end)
