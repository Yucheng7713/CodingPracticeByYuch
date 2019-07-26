# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        root = ListNode(-1)
        prev = root
        current = head
        while current and current.next:
            temp = current.next
            current.next = current.next.next
            temp.next = current
            prev.next = temp
            prev = current
            current = current.next

        return root.next