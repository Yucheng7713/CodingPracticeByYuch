# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def __init__(self):
        self.visited = dict()

    def copyRandomList_Recursive(self, head):
        if head == None:
            return None
        if head in self.visited:
            return self.visited[head]
        c_node = RandomListNode(head.label)
        self.visited[head] = c_node
        c_node.next = self.copyRandomList_Recursive(head.next)
        c_node.random = self.copyRandomList_Recursive(head.random)

        return c_node

    def copyRandomList_Iterative(selfs, head):
        if head == None:
            return None
        c_node = RandomListNode(head.label)
        root = RandomListNode(-1)
        root.next = c_node
        index = head.next
        # Copy along next pointer
        while index != None:
            new_node = RandomListNode(index.val)
            c_node.next = new_node
            c_node = c_node.next
            index = index.next
            self.visited[index] = c_node

        # Copy along random pointer
        index = head
        c_node = root.next
        while index != None:
            if index.random in self.visited:
                c_node.random = self.visited[index.random]
            elif index.random:
                c_node.random = RandomListNode(index.random.val)
            else:
                c_node.random = None
            index = index.next
            c_node = c_node.next

        return root.next


