# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        tail = head
        prev_head = head
        while tail and tail.next:
            temp = tail.next.next
            head = tail.next
            head.next = prev_head
            tail.next = temp
            prev_head = head
        return head

    def reverseList_2(self, head):
        prev_head = None
        curr_head = head
        while curr_head:
            temp = curr_head.next
            curr_head.next = prev_head
            prev_head = curr_head
            curr_head = temp
        return prev_head

    def reverseList_3(self, head: ListNode) -> ListNode:
        # The reversed result will be exactly the same if there is no node or only one node
        if not head or not head.next: return head
        # Use dummy head for convenient
        dummy = ListNode(0)
        dummy.next = current = head
        # Reverse the linked list after current index
        while current and current.next:
            temp = current.next
            current.next = current.next.next
            temp.next = dummy.next
            dummy.next = temp
        # Return the reversed linked list except the dummy node
        return dummy.next

    def reverseList_recursion(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        # Recursively call until the last node
        r_head = self.reverseList(head.next)
        # Reverse the later node pointing to the previous node
        head.next.next = head
        # Don't forget to assign head.next to None, otherwise a cycle will occur
        head.next = None
        return r_head