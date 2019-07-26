import collections

# Conditions :
# 1. use up all tickets : len(route) == len(tickets) + 1
# 2. preferably in ascending lexical order of airport code

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.route = ["JFK"]
        # initialize hash map
        flight_map = collections.defaultdict(list)
        for depart, arrival in sorted(tickets):
            flight_map[depart] += [arrival]
        # dfs traversal
        def dfs(des):
            # If all tickets are used up
            if len(self.route) == len(tickets) + 1:
                return self.route
            # Else keep traversing, find the next destination
            if des in flight_map:
                # Find a valid destination in lexical order
                for i in range(len(flight_map[des])):
                    next_des = flight_map[des].pop(i)
                    self.route += [next_des]
                    rest_route = dfs(next_des)
                    if rest_route:
                        return rest_route
                    # Reset route and flight_map for backtracking
                    self.route.pop()
                    flight_map[des].insert(i, next_des)
            else:
                return None
        return dfs("JFK")

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets_2 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(Solution().findItinerary(tickets_2))