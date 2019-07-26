import collections

# Topological sort with BFS
class Solution_I:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        indegrees = collections.defaultdict(int)
        outdegrees = collections.defaultdict(list)
        # Construct graph
        # indegrees : number of in-degree edges of each node
        # outdegrees : out-pointing adjacent nodes of each node
        for course in prerequisites:
            indegrees[course[0]] += 1
            outdegrees[course[1]] += [course[0]]
        # Find the starting point which without in-degree edge.
        start_list, topo_list = [], []
        for v in range(numCourses):
            if indegrees[v] == 0:
                start_list += [v]
        # Use BFS for topological sort
        while start_list:
            u = start_list.pop(0)
            topo_list += [u]
            for v in outdegrees[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    start_list += [v]
        print(topo_list)
        return len(topo_list) == numCourses

class Solution_II:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        graph = collections.defaultdict(list)
        # visited[v] = 0 -> v hasn't been visited yet
        # visited[v] = 1 -> v has been visited
        # visited[v] = -1 -> v is now being visited in a dfs recursion
        visited = [0] * numCourses
        for course in prerequisites:
            graph[course[1]] += [course[0]]
        def dfs(v):
            # if we confront a being visited vertax, this means there is
            # an existed cycle
            if visited[v] == -1:
                return False
            # if we confront a visited vertax, we reach a valid
            # topological order -> return True
            if visited[v] == 1:
                return True
            # Start exploring from vertax v
            visited[v] = -1
            for adj_v in graph[v]:
                if not dfs(adj_v):
                    return False
            # the vertax v has already been visited
            visited[v] = 1
            return True
        for v in range(numCourses):
            if not dfs(v):
                return False
        return True
courseNum = 6
courses = [[0, 5], [0, 4], [2, 5], [1, 4], [3, 2], [1, 3]]
print(Solution().canFinish(courseNum, courses))
