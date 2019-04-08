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
        
    def listPaths(self, i, j):
        '''Lists all possible paths from node i to node j.'''
        pass
        
    @property
    def nodes(self):
        '''Returns the set of nodes for this graph'''
        edges = list(self.edges.keys())
        nodes = [i[0] for i in edges] + [i[1] for i in edges]
        return set(nodes)
        
    @property
    def adjacencyList(self):
        '''Returns the adjacency list.'''
        ingoing, outgoing = {}, {}
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
        inDegree = {k:len(ingoing[k]) if k in ingoing else 0 for k in g.nodes}
        outDegree = {k:len(outgoing[k]) if k in outgoing else 0 for k in g.nodes}
        return inDegree, outDegree