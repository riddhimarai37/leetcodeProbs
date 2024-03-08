class Solution:
    def findMin(self, nums: List[int]) -> int:

        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = start + (end - start ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])
        # low = 0
        # high = len(nums) - 1

        # while low < high:
        #     if nums[low] < nums[high]:
        #         return nums[low]

        #     mid = low + (high-low) // 2

        #     if nums[mid] < nums[low]:
        #         high = mid 
        #     elif nums[mid] > nums[high]:
        #         low = mid + 1

        # return nums[low]

        