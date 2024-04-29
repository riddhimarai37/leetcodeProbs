class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += n
            max_sum = max(curr_sum, max_sum)

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





