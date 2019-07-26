# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        # Start from the same head index
        s_index = f_index = head
        while True:
            s_index = s_index.next
            f_index = f_index.next.next
            if s_index is f_index or not s_index or not f_index or not f_index.next:
                break
        # Reset the f_index
        f_index = head
        while s_index is not f_index and s_index and f_index:
            s_index = s_index.next
            f_index = f_index.next
        return s_index

a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b

d, e = ListNode(1), ListNode(2)
d.next = e
e.next = d

s = Solution()
print(s.detectCycle(d).val)