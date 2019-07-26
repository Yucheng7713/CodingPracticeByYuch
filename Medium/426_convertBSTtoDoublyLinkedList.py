"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def inorderTraverse(self, root: 'Node') -> 'Node':
        head, tail = root, root
        if root.left:
            left_head, left_tail = self.inorderTraverse(root.left)
            left_tail.right = root
            root.left = left_tail
            head = left_head
        if root.right:
            right_head, right_tail = self.inorderTraverse(root.right)
            right_head.left = root
            root.right = right_head
            tail = right_tail
        head.left = tail
        tail.right = head
        return (head, tail)

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root:
            head, tail = self.inorderTraverse(root)
            return head
        return None