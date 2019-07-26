import collections

# Sort by Column
class Solution:
    def minAreaRect(self, points: 'List[List[int]]') -> 'int':
        N = len(points)
        # Count the number of points with different x coordinate
        Nx = len(set(x for x, y in points))
        # Count the number of points with different y coordinate
        Ny = len(set(y for x, y in points))
        # If there is no point sharing the same x coordinate or y coordinate
        if N == Nx or N == Ny:
            # meaning their is no way for those points can form a rectangle
            return 0
        # Construct the coordinate map storing the coordinates sharing the same
        # x coordinate
        rect_x_map = collections.defaultdict(list)
        if Nx > Ny:
            for x, y in points:
                rect_x_map[x].append(y)
        else:
            for x, y in points:
                rect_x_map[y].append(x)
        min_rect = float('inf')
        last_x = dict()
        # Calculate each rectangle when reaching the rightmost edge (y2 - y1)
        for x in sorted(rect_x_map):
            # Find valid rightmost height
            cols = rect_x_map[x]
            cols.sort()
            # Looking for (y1, y2) sharing the same x coordinate
            for j, y2 in enumerate(cols):
                for i in range(j):
                    y1 = cols[i]
                    # If (y1, y2) has been seen with a previous smaller x coordinate
                    # A rectangle is identified -> check its area and update the min
                    # rectangle area
                    if (y1, y2) in last_x:
                        min_rect = min(min_rect, (x - last_x[y1, y2]) * (y2 - y1))
                    # Update the last seen x coordinate
                    last_x[y1, y2] = x
        return min_rect if min_rect < float('inf') else 0

# Check by diagnal
class Solution_II:
    def minAreaRect(self, points: 'List[List[int]]') -> 'int':
        point_set = set(map(tuple, points))
        min_rect = float('inf')
        for j, p2 in enumerate(points):
            for i in range(j):
                p1 = points[i]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in point_set \
                and (p2[0], p1[1]) in point_set:
                    min_rect = min(min_rect, abs(p2[0] - p1[0]) * abs(p2[1] - p1[1]))
        return min_rect if min_rect < float('inf') else 0

points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
print(Solution().minAreaRect(points))