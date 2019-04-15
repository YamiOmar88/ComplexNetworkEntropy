# Bosch Data Analysis: Entropy Centrality
# Author: Yamila M. Omar
# Date: 10/4/2019

import graphfile
import graph 
import lorenzcurve

# Some useful functions
# =====================
def normalize(edges):
    '''This function allows to set edge weights in a 0 to 1 scale.
    Input variable: edges (dictionary with edges (i,j) as keys and 
    weights w_ij as values.
    The function returns a new dictionary with normalized edge weights.'''
    totSum = 0
    for k,v in edges.items():
        if k[0] == 'i':
            totSum += v
    normalized_edges = {}
    for k,v in edges.items():
        normalized_edges[k] = round(v/totSum, 5)
    return normalized_edges
    
def remove_underutilized_edges(normalized_edges, tolerance=0.05):
    ''' This function removes edges whose weight is below a tolerance.
    Input variables: normalized_edges (dictionary) and tolerance (float).'''
    new_dict = {}
    for k,v in normalized_edges.items():
        if v >= tolerance:
            new_dict[k] = v
    return new_dict


# Read data
# =========
graph_to_study = input("Which graph should we study?\n Options: family1, family2, family3 and fullNetwork\n")
file = graphfile.GraphFile("data/" + graph_to_study + ".txt")
edges = file.read_edges_from_file()

# Process data
# ============
normalized_edges = normalize(edges)
most_used_edges = remove_underutilized_edges(normalized_edges, tolerance=0.05)

# Calculations / Results
# =======================
g = graph.Graph(most_used_edges)
C_H = g.entropyCentrality

for k,v in C_H.items():
    C_H[k] = abs(round(v, 5))
    
# Write to file
# =============
# file = graphfile.GraphFile("results/entropyCentrality_" + graph_to_study + ".txt")
# file.write_centrality_values_to_file(C_H)