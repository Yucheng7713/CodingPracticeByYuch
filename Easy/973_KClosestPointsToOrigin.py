class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = []
        for i in range(len(points)):
            d = math.sqrt(points[i][0]**2 + points[i][1]**2)
            distances.append((d, i))
        distances.sort(key=lambda x:x[0])
        return [points[i] for d, i in distances[:K]]