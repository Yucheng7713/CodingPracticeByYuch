from collections import defaultdict


class DAG:
    graph = defaultdict(list)
    numOfNode = 0

    def __init__(self, n):
        for i in range(n):
            self.graph[i] = []
        self.numOfNode = n

    def addEdge(self, v, u) -> bool:
        if u >= self.numOfNode or v >= self.numOfNode:
            return False
        self.graph[v] += [u]
        return True

    def dfsTraversal(self, v, path, visited):
        visited[v] = True
        path += [str(v)]
        for adj_v in self.graph[v]:
            if not visited[adj_v]:
                self.dfsTraversal(adj_v, path, visited)
        return None

dag = DAG(4)
dag.addEdge(0, 1)
dag.addEdge(1, 2)
dag.addEdge(0, 2)
dag.addEdge(2, 0)
dag.addEdge(2, 3)
dag.addEdge(3, 3)

visited = [False] * 4
traverse_path = []
dag.dfsTraversal(0, traverse_path, visited)
print("->".join(traverse_path))
