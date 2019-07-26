import heapq
import collections

class Solution:
    # Dijkstra's Algorithm
    # Since we are using Dijkstra's to update the minimum cost to each node
    # Once we've found the destination node, it's gurantee to have the minimum cost
    # But the tricky part about this problem is that we still need to check the number
    # of stops as the restriction.

    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        # Graph construction
        flight_map = collections.defaultdict(dict)
        for f in flights:
            flight_map[f[0]][f[1]] = f[2]
        # For each node, we need to track its cost and the number of stops it has remained
        # so far ( here since we are using Dijstra's, each time we need to access the
        # node with the lowest cost )
        # Note that k means we need at most k stops between src and dst
        # which means we need to get to the dst in k + 1 steps
        # ( cost, source node, number of steps remain )
        p_queue = [(0, src, K + 1)]
        while p_queue:
            cost, str_node, k = heapq.heappop(p_queue)
            # If we've found the destination, simply return its cost
            # it's guarantee to be the cheapest cost within k stops
            if str_node == dst:
                return cost
            # otherwise if there is still stop moves beyond the current node
            # keep searching and updating the costs of its adjacent nodes.
            if k > 0:
                for adj in flight_map[str_node]:
                    heapq.heappush(p_queue, (cost + flight_map[str_node][adj], adj, k-1))
        return -1

    # Dynamic Programming ( Bellman-ford )
    # Concept : we need to get to 'dst' in k + 1 steps
    # find the cheapest cost to get to 'i' node at (k+1)th step
    # we need to find the cheapest cost to get to 'i' node within K steps and so on
    # dp[i] : the cheapest cost to get to ith node in kth step
    # new_dp[i] : the cheapest cost to get to ith node in (k+1)th step
    def findCheapestPrice_DP(self, n: int, flights, src: int, dst: int, K: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0
        for i in range(K + 1):
            # Copy new_dp
            new_dp = dp[:]
            for s, d, cost in flights:
                new_dp[d] = min(new_dp[d], dp[s] + cost)
            dp = new_dp
        return dp[dst] if dp[dst] != float('inf') else -1

n = 4
flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src =  0
dst = 3
K = 1
print(Solution().findCheapestPrice_DP(n, flights, src, dst, K))