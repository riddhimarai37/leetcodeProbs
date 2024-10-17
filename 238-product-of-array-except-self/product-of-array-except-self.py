class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]

        return res





















        # res = [1] * len(nums)

        # prefix = 1
        # # populate array with prefix values
        # for idx in range(0, len(res)):
        #     res[idx] = prefix
        #     prefix *= nums[idx]

        # postfix = 1
        # for idx in range(len(res) - 1, -1 ,-1):
        #     res[idx] *= postfix
        #     postfix *= nums[idx]

        # return res
    
        # Time: O(n) Space: O(1)
        
            



