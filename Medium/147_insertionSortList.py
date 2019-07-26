# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Sort by creating a new linked list
class Solution:
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        sorted_list = ListNode(float('-inf'))
        while head:
            temp = sorted_list
            # Find the insertion position
            while temp and temp.next:
                if temp.next and temp.next.val > head.val:
                    break
                temp = temp.next
            # Insert the current sorted node into the right position
            tail = temp.next if temp else None
            new_node = ListNode(head.val)
            new_node.next = tail
            temp.next = new_node
            head = head.next
        return sorted_list.next

# Sort in-place
class Solution_II:
    def insertionSortList(self, head: 'ListNode') -> 'ListNode':
        p = sorted_list = ListNode(float('-inf'))
        current = sorted_list.next = head
        while current and current.next:
            val = current.next.val
            if current.val < val:
                current = current.next
                continue
            # If the previous inserted point's value > current value
            # Need to re-search the inserted point from the head
            if p.next.val > val:
                p = sorted_list
            while val > p.next.val:
                p = p.next
            new_node = current.next
            current.next = new_node.next
            new_node.next = p.next
            p.next = new_node
        return sorted_list.next