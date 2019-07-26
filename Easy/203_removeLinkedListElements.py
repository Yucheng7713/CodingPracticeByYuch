# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next
        r_index = head
        while r_index and r_index.next:
            if r_index.next.val == val:
                r_index.next = r_index.next.next
            else:
                r_index = r_index.next
        return head