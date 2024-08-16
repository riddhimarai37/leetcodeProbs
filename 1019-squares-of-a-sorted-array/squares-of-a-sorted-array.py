class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        l,r = 0, len(nums) - 1

        while l <= r:
            left, right = nums[l], nums[r]
            if pow(left,2) > pow(right,2):
                ans.append(pow(left,2))
                l += 1
            else:
                ans.append(pow(right,2))
                r -= 1

        return ans[::-1]

                


















        # not optimized approach 
        # neg = []
        # pos = []
        # ans = []

        # for n in nums:
        #     if n > 0 or n == 0:
        #         pos.append(n)
        #     else:
        #         neg.append(n)

        # neg = list(reversed(neg))

        # for i in range(len(neg)):
        #     neg[i] = abs(neg[i])

        # i = 0
        # j = 0

        # while i < len(neg) and j < len(pos):
        #     if neg[i] < pos[j]:
        #         ans.append(pow(neg[i],2))
        #         i+=1
        #     else:
        #         ans.append(pow(pos[j],2))
        #         j += 1

        # while i < len(neg):
        #     ans.append(pow(neg[i],2))
        #     i += 1

        # while j < len(pos):
        #     ans.append(pow(pos[j],2))
        #     j += 1

        # return ans

        # time: O(N) a few passes; O(N) helper arrays



