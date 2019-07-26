class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        def numOfBST(k):
            t_num = 0
            if dp[k] > 0: return dp[k]
            for i in range(1, k+1):
                t_num += numOfBST(i-1) * numOfBST(k-i)
            dp[k] = t_num
            return dp[k]
        return numOfBST(n)

print(Solution().numTrees(3))