class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([math.sqrt(k) for k in A])