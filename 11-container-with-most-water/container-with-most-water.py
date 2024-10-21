class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        max_area = 0

        while l < r:
            curr_area = (r-l) * min(height[l], height[r])
            max_area = max(curr_area, max_area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

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

