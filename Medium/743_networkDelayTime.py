import collections
import heapq

class Solution:
    # DFS
    # Looking for the maximum earliest signal arrival time
    # Keep track of the earliest signal arrival time for each node
    def networkDelayTime(self, times, N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for s, e, t in times:
            graph[s].append((t, e))
        # Sort in advance preventing sorting in recursion
        for n in graph:
            graph[n].sort()
        # Shorthand
        dst = {node: float('inf') for node in range(1, N + 1)}
        # dst = dict()
        # for node in range(1, N+1):
        #     dst[node] = float('inf')
        def dfs(node, elapsed_time):
            # If the node has already been reach by an earlier signal
            # Stop depth searching -> return
            if dst[node] <= elapsed_time:
                return
            # Record/Update the signal arrived time
            dst[node] = elapsed_time
            # Traverse from the node starting from smaller time path (for speed-up)
            # We hope to visit all the nodes ASAP
            for time, adj_node in graph[node]:
                dfs(adj_node, elapsed_time + time)
        dfs(K, 0)
        # Find the maximum arrival time
        ans = max(dst.values())
        # If the maximum arrival time is float('inf')
        # This means there is node which hasn't been visited -> cannot reach every node
        # return -1
        return -1 if ans == float('inf') else ans

    def networkDelayTime_II(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for s, e, t in times:
            graph[s].append((e, t))
        dst = {node: float('inf') for node in range(1, N + 1)}
        dst[K] = 0
        visited = [0] * (N + 1)
        cand_nodes = [(0, K)]
        heapq.heapify(cand_nodes)
        while cand_nodes:
            time, node = heapq.heappop(cand_nodes)
            if not visited[node]:
                for adj_node, elapsed in graph[node]:
                    dst[adj_node] = min(time + elapsed, dst[adj_node])
                    heapq.heappush(cand_nodes, (dst[adj_node], adj_node))
                visited[node] = 1
        return -1 if sum(visited) != N else max(dst.values())

    # Dijkstra's
    def networkDelayTime_III(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for s, e, t in times:
            graph[s][e] = t
        # For Dijkstra's, we need to track visited nodes
        seen = set()
        # Queue/Heap for accessing next minimum time node
        cand_nodes = [(0, K)]
        while cand_nodes:
            # Since we r using heap here, everytime we can surely get the minimum value node
            time, node = heapq.heappop(cand_nodes)
            if node in seen: continue
            seen.add(node)
            res = time
            # Even if some nodes' value get updated, we don't need to worry about such case
            # Since we are using heap, if the value get updated, we are assured to get it first.
            for adj_node in graph[node]:
                heapq.heappush(cand_nodes, (time + graph[node][adj_node], adj_node))
        return res if len(seen) == N else -1

times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(Solution().networkDelayTime_II(times, n, k))