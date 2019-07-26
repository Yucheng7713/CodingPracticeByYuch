# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        p = p_list = ListNode(float('inf'))
        p_list.next = head
        # Move until encountering a node which is the boundary between two partitions
        while p and p.next and p.next.val < x:
            p = p.next
        current = p.next
        while current and current.next:
            val = current.next.val
            # Move the node to the left partition -> insert it into the end of the left partition
            if val < x:
                new_node = current.next
                current.next = new_node.next
                new_node.next = p.next
                p.next = new_node
                p = p.next
            else:
                current = current.next
        return p_list.next