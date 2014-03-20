import matrix

def read_matrix(file_name):
    fo = open(file_name, 'r') # get file object reference
    seq = fo.readline().replace(' ', '').strip('\n')
    result = matrix.gen_matrix(len(seq), len(seq))
    p = 0
    while True:
        line = fo.readline().strip('\n').strip()
        q = 0
        if line == '':
            break
        else:
            split_line = line.split()
            for x in split_line:
                result[p][q] = int(x)
                q += 1
            p += 1
    fo.close()
    return [seq, result]