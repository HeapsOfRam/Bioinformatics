# Generates a matrix give given row size and column size all filled with
# a default initial value (ivalue) None, which is a special value in
# Python denoting nothing. The function makes use of keyword arguments.
# Thus if called, say, gen_matrix(2,3) will produce a matrix with the default
# entries None. To initialize with specific values other than None,
# make a call giving keyword argument a specific vlue.
# E.g. gen_matrix(2,3,ivalue=0). Function is defined using
# nested list comprehensions.

def gen_matrix(rows, cols, ivalue = None):
    return [[ivalue for c in range(cols)] for r in range(rows)]

# Generates a matrix give given row size and column size all filled with None,
# which is a special value in Python denoting nothing.
# Uses nested for loops

def gen_matrix_v2(rows, cols):
    result = []
    for i in range(rows):
        row = []
        for j in range(cols): # generate a row of None
            row.append(None)
        result.append(row) # add it to result list
    return result

# A simple sustitution matrix for nucleotides represented as dict of dict
# giving 1 for a mtch and -1 for a mismatch
smatrix = {'A':{'A':1, 'C':-1, 'T':-1, 'G':-1},
           'C':{'A':-1, 'C':1, 'T':-1, 'G':-1},
           'T':{'A':-1, 'C':-1, 'T':1, 'G':-1},
           'G':{'A':-1, 'C':-1, 'T':-1, 'G':1}}

# Writes a given matrix (as a list of lists) onto an html file with
# html table tags.
def gen_html_table(matrix, fname='my-table.html'):
    fo = open(fname,'w')
    fo.write('<!DOCTYPE html>\n<html>\n')
    fo.write('<head>\n<style>\n')
    fo.write('table,th,td{border:1px solid black;border-collapse:collapse;}\n')
    fo.write('tr{text-align:right;}\n</style>\n</head>\n')
    fo.write('<body><table>\n')
    for row in matrix:
        trow = '<tr>'+''.join(['<td>'+str(item)+'</td>' for item in row])+'</tr>\n'
        fo.write(trow)
    fo.write('</table>\n</body>\n</html>\n')
    fo.close()
