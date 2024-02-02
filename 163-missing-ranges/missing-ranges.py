
# [1,5] nums = [1,2,4] missing nums = [3,5] ranges = [[3,3] [5,5]]
# [] --> [lower,upper]
# [-1] --> 


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[lower,upper]]

        if lower < nums[0]:
            res.append([lower, nums[0] - 1])

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                res.append([nums[i-1] + 1, nums[i] -1])

        if upper > nums[-1]:
            res.append([nums[-1] + 1,upper])

        return res


        
        # nums = [lower-1] + nums + [upper+1]
        # results = []

        # for i in range(len(nums)-1):
        #     if nums[i+1] - nums[i] == 2:
        #         results.append([nums[i]+1, nums[i]+1])
        #     elif nums[i+1] - nums[i]>2:
        #         results.append([nums[i]+1, nums[i+1]-1])

        # return results

                
            
            




        


        