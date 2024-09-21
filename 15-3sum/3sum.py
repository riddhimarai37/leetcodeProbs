class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for idx,n in enumerate(nums):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            if n > 0:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
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
            
            
            


                




















      








