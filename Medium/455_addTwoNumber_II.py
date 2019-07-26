# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, node: 'ListNode') -> 'ListNode':
        head = tail = node
        while tail and tail.next:
            temp = tail.next.next
            tail.next.next = head
            head = tail.next
            tail.next = temp
        return head

    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        l1, l2 = self.reverseList(l1), self.reverseList(l2)
        carry = 0
        head = None
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
            sum_node.next = head
            head = sum_node
        return head