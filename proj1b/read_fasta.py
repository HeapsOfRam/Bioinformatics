# for reading FASTA file containing one sequence
def read_fasta_v1(file_name):
    result = ""
    fo = open(file_name, 'r') # get file object reference
    fo.readline() # ignore the first line
    while True:
        line = fo.readline().strip('\n')
        if line == '':
            break
        else:
            result = result + line
    fo.close()
    return result.replace('\r','') # drop \r if DOS

def read_fasta_v2(file_name):
    result = ""
    fo = open(file_name, 'r') # get file object reference
    lines = fo.readlines() # returns a list strings, one per line
    fo.close()
    lines = lines[1:] # drop the first one
    stripped_lines = [s.strip('\n') for s in lines] # drop \n from end
    return result.join(stripped_lines).replace('\r','') # drop \r if DOS