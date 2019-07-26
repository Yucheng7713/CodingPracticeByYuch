class Solution(object):
    def getIntersectionNode(self, headA, headB):
        index_A, index_B = headA, headB
        if index_A and index_B:
            while index_A or index_B:
                if not index_A and index_B:
                    index_A = headB
                elif not index_B and index_A:
                    index_B = headA
                if index_A == index_B:
                    return index_A
                index_A = index_A.next
                index_B = index_B.next
        return None