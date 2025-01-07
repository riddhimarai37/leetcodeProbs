class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()

        for idx,n in enumerate(nums):
            if n > 0:
                break

            if idx > 0 and n == nums[idx-1]:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                curr = n + nums[l] + nums[r]
                if curr == 0:
                    res.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr > 0: 
                    r -= 1
                else: 
                    l += 1

        return list(res)





















        
        # nums = sorted(nums)
        # res = []

        # for idx,num in enumerate(nums):
        #     # same as previous
        #     if idx > 0 and num == nums[idx-1]:
        #         continue

        #     l = idx + 1
        #     r = len(nums) - 1
            
        #     while l < r:
        #         # current sum
        #         three_sum = num + nums[l] + nums[r]

        #         if three_sum > 0:
        #             r -= 1
        #         elif three_sum < 0:
        #             l += 1
        #         else:
        #             res.append([num, nums[l], nums[r]])
        #             l += 1
        #             # skipping past duplpicates
        #             while nums[l] == nums[l-1] and l < r:
        #                 l += 1

        # return res

    # Time: O(n^2)
    # Space: O(1)
            
            
            


                




















      








