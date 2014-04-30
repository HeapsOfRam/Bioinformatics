import init_dict

MAX_DIST = 99999

file_in_base = "matrix_"
file_in_ext = ".txt"
file_out_base = "tree_"
file_out_ext = ".txt"
iteration = 1
choice = 0

while(choice != 1 and choice != 2):
	choice = raw_input("Enter 1 For Single Linkage and 2 For Complete Linkage: ")

	if choice != '1' and choice != '2':
		print "Error please try again"
	else:
		choice = int(choice)

print '\n'

file_in = file_in_base + str(iteration) + file_in_ext

cluster_hash = init_dict.init_dict(file_in)
print cluster_hash


while len(cluster_hash) > 1:
	minimum = MAX_DIST

	for key in cluster_hash:
		for in_key in cluster_hash[key]:
			if in_key != key:
				val = cluster_hash[key][in_key]
				if val < minimum:
					minimum = val
					min_key = key
					min_in_key = in_key

	hash_element = {}

	del cluster_hash[min_key]
	del cluster_hash[min_in_key]

	for key in cluster_hash:
		if choice == 1:
			hash_element[key] = min(cluster_hash[key][min_key], cluster_hash[key][min_in_key])

		cluster_hash[key][min_key + min_in_key] = hash_element[key]

		del cluster_hash[key][min_key]
		del cluster_hash[key][min_in_key]

	cluster_hash[min_key + min_in_key] = hash_element
	
	print len(cluster_hash)
	print cluster_hash

#print init_dict.init_dict(file_in_base + str(iteration) + file_in_ext)
