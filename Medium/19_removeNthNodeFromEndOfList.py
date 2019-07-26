# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        l = self.linkedListLength(head) - n
        root = ListNode(0)
        root.next = head
        index = root
        while l > 0:
            l -= 1
            index = index.next
        index.next = index.next.next
        return root.next

    def linkedListLength(self, head):
        l_length = 0
        while head is not None:
            l_length += 1
            head = head.next
        return l_length

    def removeNthFromEnd_II(self, head: ListNode, n: int) -> ListNode:
        if not head: return None
        # 1st pass : Find the length of the linked list L
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        # If we are removing the last element reversely -> simply return head.next
        if n == count:
            return head.next
        # If the targeted element is not in the linked list -> simply return head
        if n > count:
            return head
        # 2nd pass : Remove ( L - n )th element
        temp, prev = head, None
        count -= n
        while count > 0:
            prev = temp
            temp = temp.next
            count -= 1
        prev.next = temp.next
        return head

    def removeNthFromEnd_III(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next: return None
        # Create a dummy list node for convenient
        d = ListNode(0)
        d.next = head
        slow = fast = d
        # Move the fast index ( n + 1 ) steps forward
        count = n + 1
        while count > 0 and fast:
            fast = fast.next
            count -= 1
        # Find the reversed ( n + 1 )th element by moving both slow and fast index
        # Like window sliding method
        while fast:
            fast, slow = fast.next, slow.next
        # Remove nth element
        slow.next = slow.next.next
        return d.next

s = Solution()

a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next, b.next, c.next, d.next = b, c, d, e
i = ListNode(7)
i = s.reverseLinkedList(i.next)

while i != None:
    print(str(i.val), end="->")
    i = i.next
