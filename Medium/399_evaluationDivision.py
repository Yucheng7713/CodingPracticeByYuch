import collections


class Solution(object):
    def __init__(self):
        self.graph = collections.defaultdict(list)

    # Function for building graph
    def buildGraph(self, equations, values):
        # Add edge into the graph
        def addEdge(node_1, node_2, val):
            self.graph[node_1] += [(node_2, val)]

        for vertices, val in zip(equations, values):
            n1, n2 = vertices
            addEdge(n1, n2, val)
            addEdge(n2, n1, 1 / val)

    # Function for retrieving query
    def queryEquation(self, query):
        n1, n2 = query
        if n1 not in self.graph or n2 not in self.graph:
            return -1.0
        q = collections.deque([(n1, 1)])
        visited = set()
        while q:
            curr_node, curr_val = q.popleft()
            # If n1 == n2, n1 / n2 = 1
            if curr_node == n2:
                return curr_val
            visited.add(curr_node)
            for adj_node, value in self.graph[curr_node]:
                if adj_node not in visited:
                    q.append((adj_node, curr_val * value))
        return -1.0

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.buildGraph(equations, values)
        return [self.queryEquation(q) for q in queries]

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
Solution().calcEquation(equations, values, queries)