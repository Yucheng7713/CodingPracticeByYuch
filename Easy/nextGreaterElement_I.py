class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        g_stack, result = [], []
        g_map = dict()
        for n in nums2:
            while len(g_stack) > 0 and n > g_stack[-1]:
                g_map[g_stack.pop()] = n
            g_stack.append(n)
        for n in nums1:
            result.append(g_map.get(n, -1))
        return result
