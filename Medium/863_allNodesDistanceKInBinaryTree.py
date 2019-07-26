import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # BFS - Convert the tree into graph then perform BFS
    # Low performance
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        tree_graph = collections.defaultdict(list)
        def bfsGraphConstruct(node):
            queue = [node]
            while queue:
                frontier = []
                for n in queue:
                    if n.left:
                        tree_graph[n.val].append(n.left.val)
                        tree_graph[n.left.val].append(n.val)
                        frontier.append(n.left)
                    if n.right:
                        tree_graph[n.val].append(n.right.val)
                        tree_graph[n.right.val].append(n.val)
                        frontier.append(n.right)
                queue = frontier

        def dfsGraphConstruct(node):
            if not node:
                return
            if node.left:
                tree_graph[node.val].append(node.left.val)
                tree_graph[node.left.val].append(node.val)
            if node.right:
                tree_graph[node.val].append(node.right.val)
                tree_graph[node.right.val].append(node.val)
            dfsMapBuild(node.left)
            dfsMapBuild(node.right)

        # bfsGraphConstruct(root)
        dfsGraphConstruct(root)

        k_layer, visited = [target.val], [target.val]
        while K:
            temp_layer = []
            for node in k_layer:
                for adj in tree_graph[node]:
                    if adj not in visited:
                        visited.append(adj)
                        temp_layer.append(adj)
            k_layer = temp_layer
            K -= 1
        return k_layer

    #
    def distanceK_II(self, root, target, K):




a, b, c, d, e, f ,g, h, i = TreeNode(3), TreeNode(5), TreeNode(1), TreeNode(6), TreeNode(2), TreeNode(0), TreeNode(8), TreeNode(7), TreeNode(4)
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = f, g
e.left, e.right = h, i

x, y, z, w = TreeNode(0), TreeNode(2), TreeNode(1), TreeNode(3)
x.left, x.right = y, z
z.left = w

target = TreeNode(5)
k = 2
print(Solution().distanceK(a, target, k))