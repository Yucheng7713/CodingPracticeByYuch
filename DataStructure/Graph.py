from collections import defaultdict


class Graph:
    # Graph Construction
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.numOfVertices = vertices

    def addEdge(self, u, v):
        self.graph[u] += [v]

    # DFS Traversal
    def depthFirstSearchUtil(self, v, visited, path):
        visited[v] = True
        path += [v]
        for adj_v in self.graph[v]:
            if not visited[adj_v]:
                self.depthFirstSearchUtil(adj_v, visited, path)

    # DFS Traversal for connected graph
    # Some vertices may not be reachable if the graph is disconnected
    def depthFirstSearch(self, v):
        visited = [False] * self.numOfVertices
        path = []
        self.depthFirstSearchUtil(v, visited, path)
        return path

    # DFS Traversal for disconnected graph
    def depthFirstSearch_DAG(self, v):
        visited = [False] * self.numOfVertices
        path = []
        for i in range(self.numOfVertices):
            if not visited[i]:
                self.depthFirstSearchUtil(i, visited, path)
        return path

    # Topological Sort
    def topologicalUtil(self, v, visited, stack):
        visited[v] = True
        for adj_v in self.graph[v]:
            if not visited[adj_v]:
                self.topologicalUtil(adj_v, visited, stack)
        stack += [v]

    def topologicalSort(self):
        visited = [False] * self.numOfVertices
        stack = []
        # Do topological traverse at each node that hasn't been visited
        for i in range(self.numOfVertices):
            if not visited[i]:
                self.topologicalUtil(i, visited, stack)
        # The final stack result is the topological order of the graph
        return stack[::-1]

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 0)
    g.addEdge(5, 2)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print(g.depthFirstSearch(5))
    print(g.topologicalSort())