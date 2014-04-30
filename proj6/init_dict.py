def init_dict(file_name):
    fo = open(file_name, 'r') # get file object reference
    lines = fo.readlines() # returns a list strings, one per line
    fo.close()
    stripped_lines = [s.strip('\n') for s in lines] # drop \n from end
    stripped_lines = map(lambda x:x.replace('\r',''), stripped_lines) # remove \r if from DOS
    names = stripped_lines[0].split(' ') # header names as a list
    value_rows = stripped_lines[1:] # drop the header
    name_value_rows = [dict(zip(names,map(float,row.split(' ')))) for row in value_rows]
    return dict(zip(names, name_value_rows)) # dict of dict of rows

    
 
