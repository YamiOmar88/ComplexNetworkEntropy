# Test code

import graph
import graphfile
import pagerank

network = input("Enter family1 or family2 or family3 or fullNetwork:\n")
fileName = "data/" + network + ".txt"
edges = graphfile.GraphFile(fileName).read_edges_from_file()

# edges = {(1,2):1, (1,3):1, (1,4):1, (2,1):1, (2,4):1, (3,3):1, (4,2):1, (4,3):1}
# edges = {(1,2):1, (1,3):1, (2,3):1, (3,1):1, (4,3):1}
# edges = {(1,2):1, (2,1):1, (2,3):1, (3,1):1}
g = graph.Graph(edges)
pR = pagerank.PageRank(g, taxation_type="modified", B=0.85)

file = graphfile.GraphFile("results/pagerank_" + network + ".txt")
file.write_centrality_values_to_file(pR.pagerank)
    
    

