class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a_map = dict()
        res = []
        for b in B:
            a_map[b] = B.index(b)
        for a in A:
            res.append(a_map[a])
        return res