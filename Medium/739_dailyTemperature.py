class Solution:
    # Hash map + Stack : TLE
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        t_stack = [0]
        t_map = {0 : 0}
        for i in range(1, len(T)):
            for t in t_stack:
                t_map[t] += 1
            while t_stack and T[i] > T[t_stack[-1]]:
                t_stack.pop()
            t_stack.append(i)
            t_map[i] = 0
        return [v if k not in t_stack else 0 for k, v in t_map.items()]

t_list = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(t_list))