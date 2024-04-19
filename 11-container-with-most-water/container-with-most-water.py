class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, cur_area)

            if height[left] > height[right]:
                right -= 1
            elif height[right] > height[left]:
                left += 1
            else:
                left += 1
                right -= 1

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

        # Time: O(N)
        # Space: O(1)

