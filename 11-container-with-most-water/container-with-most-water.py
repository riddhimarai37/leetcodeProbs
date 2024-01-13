class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])

        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            area = (min(height[left], height[right]) * (right-left))
            maxArea = max(maxArea, area)
            if height[left] <= height[right]: 
                left += 1
            else:
                right -=1

        return maxArea 
            

        