from collections import defaultdict

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # Build the graph as a list hash map
        # key = node (index), value = connected nodes (index)
        graph = defaultdict(list)
        for i, s1 in enumerate(stones):
            for j in range(i):
                s2 = stones[j]
                # If both nodes share the same row or column
                # then they are connected
                if s1[0] == s2[0] or s1[1] == s2[1]:
                    graph[i] += [j]
                    graph[j] += [i]
        # DFS traverse all connected components
        ans = 0
        visited = [False] * len(stones)
        for i in range(len(stones)):
            # Start at stone ith
            # If the stone ith hasn't been visited
            if not visited[i]:
                stack = [i]
                visited[i] = True
                # Keep visiting until all nodes in the connected component is visited
                while stack:
                    # Increase the size of the component
                    ans += 1
                    n = stack.pop()
                    # Append all connected nodes for further traversal
                    for adj in graph[n]:
                        if not visited[adj]:
                            stack += [adj]
                            visited[adj] = True
                # The largest number of move =
                # size of connected component - 1
                ans -= 1
        return ans
