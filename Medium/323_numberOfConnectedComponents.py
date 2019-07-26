import collections

class Solution:
    def countComponents(self, n, edges):
        # DFS traversal
        def dfs(node, visited, graph):
            # If the node has been visited already -> return
            if visited[node]: return
            # Else mark the node as visited -> start DFS on this node recursively
            visited[node] = 1
            for adj_node in graph[node]:
                dfs(adj_node, visited, graph)

        # Constructing the graph from the list of edge pairs "edges"
        graph = collections.defaultdict(list)
        for n1, n2 in edges:
            graph[n1] += [n2]
            graph[n2] += [n1]
        visited = [0] * n
        numOfCC = 0

        # Iterate through each node from 0 ~ n - 1
        for i in range(n):
            # If the node v hasn't been visited
            if visited[i] == 0:
                dfs(i, visited, graph)
                # After DFS traversal, we have identified a complete connected component
                numOfCC += 1
        return numOfCC

    def countComponents_II(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        visited = [False] * n
        numOfCC = 0
        # Constructing the graph from the list of edge pairs "edges"
        for n1, n2 in edges:
            graph[n1] += [n2]
            graph[n2] += [n1]
        # Iterate through each node from 0 ~ n - 1
        for n, v in enumerate(visited):
            # If the node v hasn't been visited
            if not v:
                # Do BFS starting on v
                queue = [n]
                visited[n] = True
                while queue:
                    q_len = len(queue)
                    for i in range(q_len):
                        k = queue.pop(0)
                        for adj_n in graph[k]:
                            # If the adjacent node hasn't been visited
                            # Append it into the queue then mark it as visited
                            if not visited[adj_n]:
                                queue += [adj_n]
                                visited[adj_n] = True
                # After BFS ended, all nodes in the connected component including node v
                # have been visited -> we have identified a connected component
                numOfCC += 1
        return numOfCC

n = 2
edges = [[1,0]]
print(Solution().countComponents(n, edges))

