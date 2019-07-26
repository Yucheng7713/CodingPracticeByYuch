# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        val_1 = val_2 = 0
        carry = 0
        result = ListNode(-1)
        prev = result
        while l1 or l2 or carry:
            val_1 = val_2 = 0
            if l1:
                val_1 = l1.val
                l1 = l1.next
            if l2:
                val_2 = l2.val
                l2 = l2.next
            carry, sum_two = divmod(val_1 + val_2 + carry, 10)
            sum_node = ListNode(sum_two)
            prev.next = sum_node
            prev = sum_node
        return result.next




