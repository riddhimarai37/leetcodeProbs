class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []    
        nums = sorted(nums)

        for i, num in enumerate(nums):
            # if number is a duplicate
            if num == nums[i-1] and i > 0:
                continue

            # two pointer solution to find a complement 
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]

                # sum is too big
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res










        