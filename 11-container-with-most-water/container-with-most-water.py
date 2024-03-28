class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(curr_area, max_area)

            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -=1

        return max_area




























        # maxArea = 0
        # l = 0
        # r = len(height) - 1

        # while l < r:
        #     maxArea = max(maxArea,(r-l) * min(height[l], height[r]))
        #     if height[l] > height[r]:
        #         r -=1
        #     else:
        #         l +=1

        # return maxArea

