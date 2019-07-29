# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal, None)
        if not head:
            # If list is empty
            head = new_node
            new_node.next = new_node
        else:
            # If list is non-empty
            prev, current = head, head.next
            while current != head:
                if prev.val <= new_node.val <= current.val:
                    # insert in the middle
                    break
                elif prev.val > current.val and (new_node.val < current.val or new_node.val > prev.val):
                    # insert in the cycle entry point where new node value is either the smallest or the largest
                    break
                prev, current = prev.next, current.next
            # Insert the new node
            prev.next = new_node
            new_node.next = current
        return head

n1, n2, n3 = Node(3, None), Node(3, None), Node(3, None)
n1.next, n2.next, n3.next = n2, n3, n1
head = n2
return_node = Solution().insert(head, 0)
print(return_node.val)