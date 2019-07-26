class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = set()
        result = 0
        # DFS - search the hole friend circle starting from the given node
        def dfs(node):
            for stu, is_friend in enumerate(M[node]):
                # If "node" and "stu" is friend -> keep searching starting from "stu"
                if is_friend and stu not in visited:
                    visited.add(stu)
                    dfs(stu)

        for i in range(len(M)):
            # If there is a node which hasn't been visited yet -> a new friend circle is found
            # circle += 1
            if i not in visited:
                dfs(i)
                result += 1
        return result