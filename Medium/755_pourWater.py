class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        heights = [100] + heights + [100]
        K += 1
        for d in range(V):
            l_index, drop_point = K, -1
            while l_index >= 1:
                if heights[l_index] - heights[l_index - 1] > 0:
                    drop_point = l_index - 1
                elif heights[l_index - 1] - heights[l_index] > 0:
                    break
                l_index -= 1
            if drop_point >= 0:
                heights[drop_point] += 1
            else:
                r_index = K
                while r_index <= len(heights) - 2:
                    if heights[r_index] - heights[r_index + 1] > 0:
                        drop_point = r_index + 1
                    elif heights[r_index + 1] - heights[r_index] > 0:
                        break
                    r_index += 1
                if drop_point >= 0:
                    heights[drop_point] += 1
                else:
                    heights[K] += 1
        return heights[1:-1]