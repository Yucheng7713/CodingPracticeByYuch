class Solution:
    # Brute Force : Time limit exceed ( TLE )
    # Check the maximum trapped water for each ith element by
    # searching the minimum of the maximum heights in both sides.
    # the possbile trapped water will be the minimum between left and right maximum
    # subtract ith's height.
    # Time Complexity : O(N^2), Space Complexity : O(1)
    def trap_I(self, height):
        result = 0
        for i in range(len(height)):
            l_index, r_index = i - 1, i + 1
            l_max = r_max = float('-inf')
            while l_index >= 0:
                l_max = max(l_max, height[l_index])
                l_index -= 1
            while r_index < len(height):
                r_max = max(r_max, height[r_index])
                r_index += 1
            k = min(l_max, r_max)
            if k - height[i] > 0:
                result += (k - height[i])
        return result

    # Dynamic programming - store the left and right maximum
    # get rid of the inner for loop searching for maximum bounds
    # Time complexity : O(N)
    # Space complexity : O(N)
    def trap_II(self, height):
        ans, N = 0, len(height)
        if N == 0: return ans
        left_max, right_max = [0] * N, [0] * N
        left_max[0] = height[0]
        for i in range(1, N):
            left_max[i] = max(height[i], left_max[i - 1])
        right_max[N - 1] = height[N - 1]
        for i in range(N - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for j in range(N):
            ans += min(left_max[j], right_max[j]) - height[j]
        return ans

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(Solution().trap_II(heights))
bin_a = '1100'
print(int(bin_a, 2))



