import collections

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def __init__(self):
        self.visited = dict()
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        copy_node = UndirectedGraphNode(node.label)
        self.visited[node] = copy_node
        for adj in node.neighbors:
            if adj not in self.visited:
                copy_node.neighbors += [self.cloneGraph(adj)]
            else:
                self.visited[node].neighbors.append(self.visited[adj])
        return copy_node