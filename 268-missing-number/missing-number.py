class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        total_sum = 0

        for i in range(0, len(nums)+1):
            total_sum += i
        
        for n in nums:
            total_sum -= n

        return total_sum



















        # missing = len(nums)
        # for i, num in enumerate(nums):
        #     missing = missing ^ i ^ num
        # return missing

        # doesnt matter which order you XOR in as long as you XOR every value in the range 
        # with every value in nums; whatever left is the missing number b/c all other nums
        # will xor with themselves at some point
        

        # Time O(n)
        # Space O(1)