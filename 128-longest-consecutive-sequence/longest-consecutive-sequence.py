class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        while numSet:
            curr = numSet.pop()
            up, down = curr+1, curr-1
            seq_len = 1

            while up in numSet:
                numSet.remove(up)
                up += 1
            seq_len += (up-curr-1)

            while down in numSet:
                numSet.remove(down)
                down -= 1
            seq_len += (curr-down-1)

            longest = max(longest, seq_len)

        return longest



        
        



        

