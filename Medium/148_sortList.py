# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeLinkedList(self, node_1, node_2):
        p = new_head = ListNode(float('-inf'))
        while node_1 and node_2:
            if node_1.val < node_2.val:
                p.next, node_1 = node_1, node_1.next
            else:
                p.next, node_2 = node_2, node_2.next
            p = p.next
        p.next = node_1 or node_2
        return new_head.next

    def sortList(self, head: 'ListNode') -> 'ListNode':
        if not head or not head.next:
            return head
        prev = slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = None
        return self.mergeLinkedList(self.sortList(head), self.sortList(slow))