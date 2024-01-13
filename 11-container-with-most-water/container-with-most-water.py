class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height[0], height[1])

        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            left_l = height[left]
            right_l = height[right]
            length = min(left_l, right_l)
            width = right - left

            maxArea = max(maxArea, length * width)
            if left_l <= right_l: 
                left += 1
            else:
                right -=1
                
        return maxArea 
            

        