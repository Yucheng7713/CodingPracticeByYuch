import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Use heap to populate the minimum node among the lists
    def mergeKLists(self, lists):
        heap = []
        # Store the candidate minimum nodes to the heap
        for i, l_node in enumerate(lists):
            if l_node:
                heap += [(l_node.val, i, l_node)]
        heapq.heapify(heap)

        temp = result = ListNode(0)
        while heap:
            # Each time pop the minimum node from the heap
            # The popped node is guarantee to be the minimum node among the lists
            n_value, seq, n = heapq.heappop(heap)
            # If there is still node behind the popped node, push it into the heap
            if n.next:
                heapq.heappush(heap, (n.next.val, seq, n.next))
            # Regular node concatenation
            temp.next = n
            temp = temp.next
        return result.next

a, b, c = ListNode(1), ListNode(4), ListNode(5)
a.next, b.next = b, c
d, e, f = ListNode(1), ListNode(3), ListNode(4)
d.next, e.next = e, f
g, h = ListNode(2), ListNode(6)
g.next = h
print(Solution().mergeKLists([a, d, g]))
