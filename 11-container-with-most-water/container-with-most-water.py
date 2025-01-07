class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0 
        l = 0
        r = len(height) - 1

        while l < r:
            curr_area = min(height[l], height[r]) * (r-l)

            if height[l] > height[r]:
                r -= 1
            elif height[r] > height[l]:
                l +=1 
            else:
                l += 1
                r -= 1
            
            max_area = max(max_area, curr_area)

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

