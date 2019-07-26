# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        l_index = f_index = head
        while f_index != None and f_index.next != None:
            l_index = l_index.next
            f_index = f_index.next.next
            if l_index == f_index:
                return True
        return False