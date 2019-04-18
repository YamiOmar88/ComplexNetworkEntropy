# Bosch Data Analysis: Entropy Centrality
# Author: Yamila M. Omar
# Date: 10/4/2019

import graphfile
import graph 
import dotfile

# Read data
# =========
while True:
    graph_to_study = input("Which graph should we study?\nOptions: family1, family2, family3 and fullNetwork\n")
    if graph_to_study in ["family1", "family2", "family3", "fullNetwork"]: 
        break
    else:
        print("Enter a valid option!\n")

file = graphfile.GraphFile("data/" + graph_to_study + ".txt")
edges = file.read_edges_from_file()

# Process data
# ============
g = graph.Graph(edges)
most_used_edges = g.remove_underutilized_edges(tolerance=0.001)
new_g = graph.Graph(most_used_edges)

# Calculations / Results
# =======================
C_H = new_g.entropyCentrality

for k,v in C_H.items():
    C_H[k] = abs(v)
    
# Write to file
# =============
file = graphfile.GraphFile("results/entropyCentrality_" + graph_to_study + ".txt")
file.write_centrality_values_to_file(C_H)


# Read C_H from file
# ==================
C_H = graphfile.GraphFile("results/entropyCentrality_" + graph_to_study + ".txt").read_centrality_values_from_file()

# Make dot file
# =============
filename = "entropyCentrality_" + graph_to_study + ".dot" 
graph_names = {"family1": "F1", "family2": "F2", "family3": "F3", "fullNetwork": "FN"}
dot = dotfile.DOT_File(filename, graph_names[graph_to_study], new_g, C_H)
dot.save()