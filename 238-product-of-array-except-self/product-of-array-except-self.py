class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[0]
        res = [1] * len(nums)

        for idx in range(1, len(res)):
            res[idx] = prefix
            prefix *= nums[idx]

        postfix = 1

        for idx in range(len(res) - 1, -1, -1):
            res[idx] *= postfix
            postfix *= nums[idx] 

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
        
            



