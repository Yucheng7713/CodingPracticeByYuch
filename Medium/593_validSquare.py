class Solution:
    # Calculate the distances between each point and see if those distances satisfy properties of a valid square
    # A valid square has :
    #       - 4 edges with same length
    #       - 2 diagnal edges with same length

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distanceCalculate(x, y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2

        points = [p1, p2, p3, p4]
        sides = collections.Counter()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                sides[distanceCalculate(points[i], points[j])] += 1
        return len(sides.keys()) == 2 and 4 in sides.values() and 2 in sides.values()