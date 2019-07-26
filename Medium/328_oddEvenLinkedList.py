# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head
        odd, even = head, head.next
        while even and even.next:
            next_odd = even.next
            even.next = next_odd.next
            next_odd.next = odd.next
            odd.next = next_odd
            odd, even = odd.next, even.next
        return head