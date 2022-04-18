from collections import defaultdict
import copy

class Graph:

    # Graph structure initialization
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.numOfVertices = vertices

    def setGraph(self, graph):
        self.graph = graph
        self.numOfVertices = len(graph.keys())

    # Graph creating method by adding edge
    def addEdge(self, u, v):
        self.graph[u] += [v]
        self.graph[v] += [u]

    # Check if a cycle will be yielded by adding the given edge.
    def cycleDetect(self):
        visited = [False] * self.numOfVertices
        for v in range(self.numOfVertices):
            if not visited[v]:
                if self.cycleDetectingHelper(v, -1, visited):
                    return True
        return False

    def cycleDetectingHelper(self, v, parent, visited):
        visited[v] = True
        for adj_v in self.graph[v]:
            if not visited[adj_v]:
                if self.cycleDetectingHelper(adj_v, v, visited):
                    return True
            else:
                if adj_v != parent:
                    return True
        return False



weight_ranklist = defaultdict(list)
weightResult, edgeResult = [], []
minimumCost = 0
vertices = set()


# Fetch graph information from text file
input_graph = open('testcases/kruskal_graph.txt', 'r')
lines = input_graph.readlines()

for line in lines:
    args = line.split(',')
    weight_ranklist[int(args[2])] += [(args[0], args[1])]
    vertices.add(args[0])
    vertices.add(args[1])

numOfVertices = len(vertices)
vertices = set()


g = Graph(numOfVertices)

for weight in sorted(weight_ranklist.keys()):
    while weight_ranklist[weight]:
        u, v = weight_ranklist[weight].pop()
        mocked_g = Graph()
        mocked_g.setGraph(copy.deepcopy(g.graph))
        mocked_g.addEdge(u, v)
        if not mocked_g.cycleDetect():
            g.addEdge(u, v)
            weightResult += [w]
            edgeResult += [(u, v)]
            minimumCost += w
            vertices.add(u)
            vertices.add(v)
        if len(vertices) == numOfVertices:
            break
    if len(vertices) == numOfVertices:
        print("MST has been found!")
        break


print("The edges of Minimum Cost Spanning Tree are ")
for i in range(len(weightResult)):
    print("{} edge <{},{}> = {}".format(i, edgeResult[i][0], edgeResult[i][1], weightResult[i]))

print("Minimum cost = {}".format(minimumCost))










