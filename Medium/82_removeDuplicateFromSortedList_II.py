# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        # Add a dummy head for convenient ( in case duplicate occurs at th head )
        slow = dummy = ListNode(0)
        fast = dummy.next = head
        while fast and fast.next:
            if fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                fast = fast.next
                slow.next = fast
            else:
                slow = fast
                fast = fast.next
        return dummy.next


