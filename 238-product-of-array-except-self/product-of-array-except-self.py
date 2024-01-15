class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1,1
        answers = [1] * len(nums) 

        for i,curr in enumerate(nums):
            answers[i] *= prefix
            prefix *= curr

        for idx in range(len(nums)-1, -1, -1):
            answers[idx] *= postfix
            postfix *= nums[idx]

        return answers 
        
            



