class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
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