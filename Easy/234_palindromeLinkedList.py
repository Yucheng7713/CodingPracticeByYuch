# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        # Find the median of the linked list
        l_index = f_index = head
        while f_index and f_index.next:
            f_index = f_index.next.next
            l_index = l_index.next
        # Reverse the second half of linked list
        i_node = None
        while l_index:
            temp = l_index.next
            l_index.next = i_node
            i_node = l_index
            l_index = temp
        # Check if the first half and the second half are identical
        while head and i_node:
            if head.val != i_node.val:
                return False
            head, i_node = head.next, i_node.next
        return True