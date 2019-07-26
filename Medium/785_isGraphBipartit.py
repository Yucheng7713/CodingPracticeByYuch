# Use BFS - color adjacent nodes with different color
# If there is adjacent nodes with same color -> return False
class Solution:
    def isBipartite(self, graph: 'List[List[int]]') -> 'bool':
        n = len(graph)
        colored_nodes = dict()
        color = 'R'
        for i in range(n):
            if i not in colored_nodes:
                colored_nodes[i] = color
                queue = [i]
                while queue:
                    node_1 = queue.pop(0)
                    color = 'B' if colored_nodes[node_1] == 'R' else 'R'
                    adj_nodes = graph[node_1]
                    for node_2 in adj_nodes:
                        if node_2 not in colored_nodes:
                            colored_nodes[node_2] = color
                            queue += [node_2]
                        elif colored_nodes[node_1] == colored_nodes[node_2]:
                            return False
        return True

graph = [[1,4],[0,2],[1],[4],[0,3]]
print(Solution().isBipartite(graph))