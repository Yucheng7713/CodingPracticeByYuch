# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        merged_list = ListNode(0)
        merged_index = merged_list
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                merged_index.next = l1
                merged_index = merged_index.next
                l1 = l1.next
            elif l1.val > l2.val:
                merged_index.next = l2
                merged_index = merged_index.next
                l2 = l2.next
        if l1 != None:
            merged_index.next = l1
        elif l2 != None:
            merged_index.next = l2

        return merged_list.next
