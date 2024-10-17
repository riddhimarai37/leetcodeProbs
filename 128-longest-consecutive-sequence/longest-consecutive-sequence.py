class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        curr_max = 0
        maximum = 0

        for n in nums: 
            curr_max = 1
            if n-1 not in set_nums:
                while n+1 in set_nums:
                    curr_max += 1
                    n +=1 
            maximum = max(curr_max, maximum)

            
        return maximum
            


















        # set_nums = set(nums)
        # longest = 0

        # for n in set_nums:
        #      # check if current number is start of a sequence 
        #     if (n-1) not in set_nums:
        #         length = 1
        #         while n+length in set_nums:
        #             length += 1
        #         longest = max(longest, length)

        # return longest
                    

        # o(N) time o(N) space
                

                

