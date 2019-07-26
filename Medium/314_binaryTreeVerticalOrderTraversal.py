# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        v_map = collections.defaultdict(list)
        t_queue = [(root, 0)]
        while t_queue:
            k = len(t_queue)
            for i in range(k):
                node, index = t_queue.pop(0)
                v_map[index].append(node.val)
                if node.left: t_queue.append((node.left, index - 1))
                if node.right: t_queue.append((node.right, index + 1))
        return [v for k, v in sorted(v_map.items())]