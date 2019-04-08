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
    '''Write G to file. G must be a dictionary. Either keys are tuples (i,j)
       of edges and values are weights w_ij, or keys are nodes i and values 
       are a property (pageRank, betweenness, etc).'''
    with open(fileName, 'w') as f:
        for k,v in G.items():
            if isinstance(node, tuple):
                i, j, w_ij = str(k[0]), str(k[1]), str(v)
                f.write(i + ' ' + j + ' ' + w_ij + '\n')
            else:
                i, p = str(k), str(v)
                f.write(i + ' ' + p + '\n')
    return True