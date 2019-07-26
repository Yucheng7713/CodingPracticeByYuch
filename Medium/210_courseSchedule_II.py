class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        visited = [0] * numCourses
        for course in prerequisites:
            graph[course[1]] += [course[0]]

        def dfs(v, schedule):
            if visited[v] == -1:
                return False
            if visited[v] == 1:
                return True
            visited[v] = -1
            for adj_v in graph[v]:
                if not dfs(adj_v, schedule):
                    return False
            visited[v] = 1
            schedule += [v]
            return True

        schedule = []
        for v in range(numCourses):
            if not dfs(v, schedule):
                return []
        return schedule[::-1]