# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMiddleNode(self, node):
        s_index = f_index = node
        prev_index = None
        while f_index and f_index.next:
            f_index = f_index.next.next
            prev_index = s_index
            s_index = s_index.next
        if prev_index:
            prev_index.next = None
        return s_index

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        middle = self.getMiddleNode(head)
        if head.val == middle.val: head = None
        root = TreeNode(middle.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(middle.next)
        return root

l1, l2, l3, l4, l5 = ListNode(-10), ListNode(-3), ListNode(0), ListNode(5), ListNode(9)
l1.next, l2.next, l3.next, l4.next = l2, l3, l4, l5
Solution().sortedListToBST(l1)
print("Done")