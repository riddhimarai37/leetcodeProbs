class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res





















        
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
            
            
            


                




















      








