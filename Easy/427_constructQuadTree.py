
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def isLeaf(self, grid):
        N = len(grid)
        return all(grid[0][0] == grid[i][j] for i in range(N) for j in range(N))
    def construct(self, grid) -> 'Node':
        if not grid: return None
        if self.isLeaf(grid):
            return Node(grid[0][0], True, None, None, None, None)
        n = len(grid) // 2
        tL = self.construct([row[:n] for row in grid[:n]])
        tR = self.construct([row[n:] for row in grid[:n]])
        bL = self.construct([row[:n] for row in grid[n:]])
        bR = self.construct([row[n:] for row in grid[n:]])
        root = Node('*', False, tL, tR, bL, bR)
        return root

grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
n = len(grid) // 2
print([row[:n] for row in grid[:n]])