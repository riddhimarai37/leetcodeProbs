class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,num in enumerate(nums):
            if num > 0:
                break

            # if you come across a duplicate
            if i > 0 and num == nums[i-1]:
                continue

            # find two nums that add up to 0 with num
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r-=1 
                    # skip over duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
            



        


