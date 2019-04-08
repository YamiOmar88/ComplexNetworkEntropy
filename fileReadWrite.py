# Useful functions
# Author: Yamila M. Omar
# Date: 4/4/2019
# ======================

def read_graph_from_file(fileName):
    '''Read graph from file. The file contains one edge per line and 
       its weight as follows:
       i j w_ij'''
    G = {}
    fileHandle = open(fileName)
    
    for line in fileHandle:
        line = line.strip().split()
        i, j, w_ij = line[0], line[1], line[2]
        
        try:
            i = int(i)
        except ValueError:
            pass
        
        try:
            j = int(j)
        except ValueError:
            pass
        
        w_ij = int(w_ij)
        G[(i,j)] = w_ij 
        
    fileHandle.close()
    return G
    
    
    
def write_graph_to_file(G, fileName):
    '''Write G to file. G must be a dictionary. Keys are tuples (i,j)
       of edges and values are weights w_ij.'''
    with open(fileName, 'w') as f:
        for k,v in G.items():
            i, j, w_ij = str(k[0]), str(k[1]), str(v)
            f.write(i + ' ' + j + ' ' + w_ij + '\n')
    return True
    
    
    
def read_centrality_values_from_file(fileName):
    '''Read centrality values from file. The file contains one node per 
    line and its centrality value as follows:
    i c_i'''
    C = {}
    with open(fileName) as f:
        for line in f:
            line = line.strip().split()
            i, c_i = line[0], float(line[1])
            
            try:
                i = int(i)
            except ValueError:
                pass 
            
            C[i] = c_i
    return C
    
    

def write_centrality_values_to_file(C, fileName):
    '''Write centrality values to file. C must be a dictionary. Keys are
       nodes i and values are centrality values c_i.'''
    with open(fileName, 'w') as f:
        for k,v in C.items():
            i, c_i = str(k), str(v)
            f.write(i + ' ' + c_i + '\n')
    return True