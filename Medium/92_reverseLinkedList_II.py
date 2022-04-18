from DataStructure.LinkedList import *

class Solution:
    def getReverseIndex(self, node, i):
        l_index = None
        r_index = node
        count = i
        while count > 0:
            l_index = r_index
            r_index = r_index.next
            count -= 1
        return l_index, r_index

    def reverseList(self, node):
        head = tail = node
        while tail and tail.next:
            temp = tail.next.next
            tail.next.next = head
            head = tail.next
            tail.next = temp
        return head, tail

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev, r_head = self.getReverseIndex(head, m - 1)
        r_tail, later = self.getReverseIndex(head, n)
        r_tail.next = None
        r_head, r_tail = self.reverseList(r_head)
        if prev:
            prev.next = r_head
        else:
            head = r_head
        r_tail.next = later
        while r_tail and r_tail.next: r_tail = r_tail.next
        return head, r_tail

    # def reverseBetween_II(self, head: ListNode, m: int, n: int) -> ListNode:
    #     if m == n or not head or not head.next: return head
    #     t1 = d = ListNode(0)
    #     d.next = head
    #     count = m
    #     # Find the reversed sublist starting index
    #     while count > 1:
    #         t1 = t1.next
    #         count -= 1
    #     current = t1.next
    #     # Start doing reverse until mth index ( we will need to do n - m times reversing )
    #     count = n - m
    #     while count > 0 and current.next:
    #         t2 = current.next
    #         current.next = current.next.next
    #         t2.next = t1.next
    #         t1.next = t2
    #         count -= 1
    #     return d.next



mylist = LinkedList()
mylist.addAtTail(1)
mylist.addAtTail(2)
mylist.addAtTail(3)
mylist.addAtTail(4)
mylist.addAtTail(5)

# mylist.head, mylist.tail = Solution().reverseList(mylist.head)
mylist.head, mylist.tail = Solution_II().reverseBetween(mylist.head, 2, 4)
print("Finish")