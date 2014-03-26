def file_open(fname):
	global fo
	fo = open(fname,'w')
	#fo.write("> Assembly Data\n")

def file_output(data):
	fo.write(str(data) + '\n')

def file_close():
	fo.close()

def file_write(fname, data):
	file_open(fname)
	file_output(str(data))
	file_close()