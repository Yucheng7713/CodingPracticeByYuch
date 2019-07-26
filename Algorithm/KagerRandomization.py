import collections
import math
from copy import deepcopy
import random

class MinimumCut:
    def __init__(self):
        self.graph = collections.defaultdict(list)
        self.numOfNode = 0
        self.numOfEdge = 0
        self.current_minCutSize = float('inf')
        self.minCutSet = set()

    # Main function
    def kagarRandomization(self):
        # Number of trials to guarantee high probability
        # n = math.ceil(((self.numOfNode ** 2 - self.numOfNode) / 2) * math.log10(self.numOfNode))
        n = 1000
        for i in range(n):
            # Copy original graph for graph initialization
            copy_g = deepcopy(self.graph)
            self.current_minCutSize = min(self.current_minCutSize, self.contraction(copy_g))
        return self.current_minCutSize

    # Pick a random edge
    def randomEdge(self, g):
        u = list(g.keys())[random.randint(0, len(g) - 1)]
        v = g[u][random.randint(0, len(g[u]) - 1)]
        return (u, v)

    # Kagar's algorithm implementation
    def contraction(self, t_graph):
        random_list = []
        # If there are more than 2 vertices
        while len(t_graph) > 2:
            # Pick a random edge
            r_edge = self.randomEdge(t_graph)
            random_list += [r_edge]
            # Contract the random edge
            self.contractEdge(t_graph, r_edge)
        # Return the size of minimum cut
        return len(t_graph[list(t_graph.keys())[0]])

    # Edge contraction function
    def contractEdge(self, t_graph, edge):
        t_graph[edge[0]].extend(t_graph[edge[1]])
        del t_graph[edge[1]]
        # Change the merged vertex to merging vertex
        for v in t_graph:
            t_graph[v] = [edge[0] if merged_v == edge[1] else merged_v for merged_v in t_graph[v]]
        # Remove self loop
        t_graph[edge[0]] = [new_v for new_v in t_graph[edge[0]] if new_v != edge[0]]

    # Read and construct the graph from reading
    def graphConstruct(self):
        gf = open("kagar_MinCut_0.txt","r")
        adj_graph = gf.read().split('\n')
        self.numOfNode = len(adj_graph)
        for adj in adj_graph:
            n_list = adj.split('\t')
            self.graph[n_list[0]] = [n for n in n_list[1:] if n != '']
            self.numOfEdge += len(self.graph[n_list[0]])
        self.numOfEdge //= 2
        gf.close()

m = MinimumCut()
m.graphConstruct()
print(m.kagarRandomization())