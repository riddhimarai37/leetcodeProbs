class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 1
        min_prod = 1
        res = nums[0]

        for n in nums:
            temp = max_prod * n 
            max_prod = max(n * min_prod, n * max_prod, n)
            min_prod = min(min_prod * n, temp, n)
            res = max(res, max_prod)

        return res



















        
        # O(n)/O(1) : Time/Memory
        # res = nums[0]
        # curMin, curMax = 1, 1

        # for n in nums:
        #     tmp = curMax * n
        #     curMax = max(n * curMax, n * curMin, n)
        #     curMin = min(tmp, n * curMin, n)
        #     res = max(res, curMax)
        # return res
        

        