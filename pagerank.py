# ======================================================================
# ======================================================================
# Page Rank Algorithm
# See: Chapter 5 in "Mining Massive Datasets" Second Edition from 
# Jure Leskovec, Anand Rajaraman and Jeffrey David Ullman.
# ======================================================================
# ======================================================================

class PageRank:
    def __init__(self, G, taxation_type="traditional", B=0.85, biased_node_list=None):
        '''Initialize PageRank object. Input variables:
        - G: Graph object.
        - taxation_type: string. Allowed values are traditional, biased
        or modified.
        - B: float. It's a constant that accounts for the probability of 
        teleportation. Usual values are between 0.8 and 0.9.
        - biased_node_list: for biased and modified pageRank calculations, 
        if the graph does not contain an i node, a list of tuples (n,w) 
        should be provided. n is the node, w is the weight that the edge 
        (i,n) would have.'''
        self.transition_matrix = self._makeMatrix(G)
        self.taxation_vector = self._makeVectorE(G, taxation_type, biased_node_list)
        self.pagerank = self._pageRank(G, B)
        
    
    def _makeMatrix(self, G):
        '''Construct transition matrix for pageRank calculation.
        Input variables:
        - G: Graph object.'''
        degreeSum = {n:0 for n in G.nodes}
        for i in G.nodes:
            for j in G.nodes:
                degreeSum[i] = degreeSum[i] + G.edges.get((i, j), 0)
    
        matrix = {}    
        for k in G.edges.keys():
            matrix[k] = G.edges[k] / degreeSum[k[0]]
            
        return matrix
        
        
    def __makeVectorE_biased(self, G, biased_node_list):
        '''Internal function to calculate vector E for biased 
        pageRank calculation.'''
        v = {k:0.0 for k in G.nodes}
        number_nodes = 0
        
        if 'i' in G.nodes:
            for k in self.transition_matrix.keys():
                if k[0] == 'i':
                    number_nodes += 1
                    v[k[1]] = 1
        elif biased_node_list != None:
            for t in biased_node_list:
                n,w = t[0], t[1]
                number_nodes += 1
                v[n] = 1
        else:
            raise ValueError("Graph does not contain i node, and biased_node_list not provided.")
            
        return {k:val/number_nodes for k,val in v.items()}
        
        
    def __makeVectorE_modified(self, G, biased_node_list):
        '''Internal function to calculate vector E for modified 
        pageRank calculation.'''
        v = {k:0.0 for k in G.nodes}
        number_nodes = 0
        
        if 'i' in G.nodes:
            for k in self.transition_matrix.keys():
                if k[0] == 'i':
                    number_nodes += 1
                    v[k[1]] = self.transition_matrix[k]
        elif biased_node_list != None:
            total_w = sum([w for (n,w) in biased_node_list])
            for t in biased_node_list:
                n,w = t[0], t[1]
                number_nodes += 1
                v[n] = w/total_w
        else:
            raise ValueError("Graph does not contain i node, and biased_node_list not provided.")
            
        return {k:val/number_nodes for k,val in v.items()}
        
        
    
    def _makeVectorE(self, G, taxation_type, biased_node_list):
        '''Construct taxation vector E. Input variables:
        - G: Graph object.
        - taxation_type: string indicating the taxation vector to be
        constructed. Possible values are
            * traditional: random walker may teleport to all nodes with 
            equal probability,
            * biased: random walker may teleport to nodes connected to 
            node i with equal probability. The rest of the nodes have 
            a value of 0,
            * modified: same as biased but the teleport set of nodes 
            have a probability related to the actual material flows.
        - biased_node_list: list of nodes for biased and modified 
        pageRank calculation. Only needed if node i is not present.'''
        if taxation_type == "traditional":
            number_nodes = len(G.nodes)
            v = {k:1.0/number_nodes for k in G.nodes}
            
        elif taxation_type == "biased":
            v = self.__makeVectorE_biased(G, biased_node_list)
                    
        elif taxation_type == "modified":
            v = self.__makeVectorE_modified(G, biased_node_list)
            
        else:
            raise ValueError("Taxation types allowed are traditional, biased or modified.")
            
        return v
        
        
    def _pageRank(self, G, B):
        '''Calculate pageRank. Input variables:
        - G: Graph object. 
        - B: float. It's a constant that accounts for the probability of 
        teleportation. Usual values are between 0.8 and 0.9.'''
        number_nodes = float( len(G.nodes) )    
        v = {n: 1/number_nodes for n in G.nodes}
        vp = {n: 0.0 for n in G.nodes}
        while any([abs(i - j) for i,j in zip(vp.values(), v.values())]) > 0.00001:
            for n in G.nodes:
                mult = 0
                for m in G.nodes:
                    mult = mult + self.transition_matrix.get((m, n), 0) * v[m]
                vp[n] = B * mult + (1 - B) * self.taxation_vector[n]
            v, vp = vp.copy(), v.copy()
          
        return vp