# Entropy Centrality
# Author: Yamila M. Omar
# Date: 5/4/2019

class Graph:
    def __init__(self, edges=dict()):
        '''Initializes a Graph. Variables:
            - edges: dictionary with edge tuples as keys (i,j) and
            weight w_ij as values.'''
        self.edges = edges
        
    
    def addEdge(self, i, j, w_ij):
        '''Allows to add and edge (i,j) and its weight w_ij to the graph'''
        self.edges[(i,j)] = w_ij
        
    
    def deleteEdge(self, i, j):
        '''Allows to delete an edge (i,j) and its associated weight'''
        try:
            self.edges.pop((i,j))
        except KeyError:
            print("{0} cannot be deleted. {0} in Graph.".format((i,j)))
        
    
    def searchPaths(self, i, j, visited, path):
        '''Searches all possible paths from node i to node j.'''
        # Set current node as visited and store it in path 
        visiting = dict(visited) 
        visiting[i] = True 
        aux = list(path)
        aux.append(i)
        # If current node is not same as destination, recursively
        # search adjacent nodes.  
        all_paths = []        
        if i != j:
            for u in self.adjacencyList[1].get(i, []):
                if visited[u] == False:
                    all_paths += self.searchPaths(u, j, visiting, aux)
        else:
            all_paths += [aux[:]]
        return all_paths

    def printAllPaths(self, i, j):
        '''Print all possible paths from node i to node j.'''
        # Set all nodes as not visited 
        visited = {n: False for n in self.nodes}
        # Create a list to store the path 
        path = []
        # Call recursive function to search for paths
        return self.searchPaths(i, j, visited, path)
        
        
    @property
    def nodes(self):
        '''Returns the set of nodes for this graph'''
        edges = list(self.edges.keys())
        nodes = [i[0] for i in edges] + [i[1] for i in edges]
        return set(nodes)
        
    
    @property
    def adjacencyList(self):
        '''Returns the adjacency list.'''
        ingoing, outgoing = {k:[] for k in self.nodes}, {k:[] for k in self.nodes}
        for edge in self.edges.keys():
            i, j = edge[0], edge[1]
            outgoing[i] = outgoing.get(i, []) + [j]
            ingoing[j] = ingoing.get(j, []) + [i]
        ingoing = {k:set(v) for k,v in ingoing.items()}
        outgoing = {k:set(v) for k,v in outgoing.items()}
        return ingoing, outgoing
        
    
    @property
    def degree(self):
        '''Calculate the degree of each node.'''
        ingoing, outgoing = self.adjacencyList
        inDegree = {k:len(ingoing[k]) if k in ingoing else 0 for k in self.nodes}
        outDegree = {k:len(outgoing[k]) if k in outgoing else 0 for k in self.nodes}
        return inDegree, outDegree
        
        
    @property
    def strength(self):
        '''Calculate the strength of each node.'''
        inStrength, outStrength = {k:0 for k in self.nodes}, {k:0 for k in self.nodes}
        for edge,weight in self.edges.items():
            i, j = edge[0], edge[1]
            inStrength[j] = inStrength[j] + weight 
            outStrength[i] = outStrength[i] + weight
        return inStrength, outStrength