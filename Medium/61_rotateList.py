# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        def rotateByOne(node: 'ListNode') -> 'ListNode':
            temp, prev = node, None
            while temp and temp.next:
                prev = temp
                temp = temp.next
            if prev:
                prev.next = temp.next
            temp.next = node
            node = temp
            return node
        if not head or not head.next: return head
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length += 1
        k %= length
        while k > 0:
            head = rotateByOne(head)
            k -= 1
        return head