class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = float('-inf')
        while left < right:
            h, w =  min(height[left], height[right]), right - left
            max_area = max(max_area, h * w)
            # Exclude the smaller boundary, only keep the higher boundary for larger
            # possible
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
