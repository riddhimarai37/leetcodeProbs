class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            curr = 1
            if (n-1) not in num_set: 
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
            




            


















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
                

                

