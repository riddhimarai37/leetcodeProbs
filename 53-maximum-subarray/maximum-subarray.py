class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        max_sum = nums[0]

        for n in nums:
            if cur < 0:
                cur = 0 
            cur += n
            max_sum = max(max_sum, cur)

        return max_sum


            

















        
        # max_sum = nums[0]
        # curr_sum = 0

        # for num in nums:
        #     if curr_sum < 0:
        #         curr_sum = 0
        #     curr_sum += num
        #     max_sum = max(max_sum, curr_sum)

        # return max_sum 

        #Time: O(n) Space: O(1)





