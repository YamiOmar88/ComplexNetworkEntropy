# Bosch Data Analysis: Entropy Centrality
# Author: Yamila M. Omar
# Date: 10/4/2019

import graphfile
import graph 
import lorenzcurve

# Read data
# =========
graph_to_study = input("Which graph should we study?\n Options: family1, family2, family3 and fullNetwork\n")
file = graphfile.GraphFile("data/" + graph_to_study + ".txt")
edges = file.read_edges_from_file()

# Process data
# ============
g = graph.Graph(edges)
most_used_edges = g.remove_underutilized_edges(tolerance=0.05)
new_g = graph.Graph(most_used_edges)

# Calculations / Results
# =======================
# C_H = new_g.entropyCentrality

# for k,v in C_H.items():
    # C_H[k] = abs(round(v, 5))
    
# Write to file
# =============
# file = graphfile.GraphFile("results/entropyCentrality_" + graph_to_study + ".txt")
# file.write_centrality_values_to_file(C_H)