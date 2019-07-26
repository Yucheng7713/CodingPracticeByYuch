from DataStructure.LinkedList import *

class Solution:
    def revertedList(self, head):
        tail = head
        while tail and tail.next:
            temp = head
            head = tail.next
            tail.next = tail.next.next
            head.next = temp
        return head

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        prev = slow
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if fast:
            slow = slow.next
            prev = prev.next
        if prev:
            prev.next = None
        slow = self.revertedList(slow)
        while slow:
            temp_1 = head.next
            temp_2 = slow.next
            head.next = slow
            slow.next = temp_1
            head = temp_1
            slow = temp_2

    # For reversing the post part of linked list recursively
    def reverse(self, head):
        if not head or not head.next: return head
        p = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return p

    def reorderList_II(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head:
            slow = fast = head
            prev = None
            # Find the middle node of the linked list
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if fast:
                prev = slow
            # Reverse the post part starting at the middle node
            # We need to keep tracking the previous node of the middle node
            prev.next = self.reverse(prev.next)
            # Interlock the first and second part of the linked list
            t1, t2 = head, prev.next
            while t1.next != t2:
                prev.next = t2.next
                t2.next = t1.next
                t1.next = t2
                t1 = t1.next.next
                t2 = prev.next

my_list = LinkedList()
my_list.addAtTail(1)
my_list.addAtTail(2)
my_list.addAtTail(3)
my_list.addAtTail(4)
Solution().reorderList(my_list.head)

