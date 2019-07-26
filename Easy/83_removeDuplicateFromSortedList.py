class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        s_index = f_index = head
        while s_index is not None:
            if f_index:
                if s_index.val == f_index.val:
                    f_index = f_index.next
                else:
                    if s_index.next != f_index:
                        s_index.next = f_index
                    s_index = f_index
            else:
                s_index.next = None
                s_index = None
        return head

    def deleteDuplicates_II(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow = fast = head
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = fast
        return head

    def deleteDuplicates_III(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head