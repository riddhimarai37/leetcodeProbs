class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    # def missingNumber(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     ans = 0

    #     for i in range(1, n+1):
    #         ans = ans ^ i
    #     for num in nums:
    #         ans = ans ^ num
    #     return ans


        # Time O(n)
        # Space O(1)