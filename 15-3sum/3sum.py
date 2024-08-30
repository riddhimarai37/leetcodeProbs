class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for idx,num in enumerate(nums):
            # same as previous
            if idx > 0 and num == nums[idx-1]:
                continue

            l = idx + 1
            r = len(nums) - 1
            
            while l < r:
                # current sum
                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    # skipping past duplpicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res

                
            
            
            


                




















        
        # res = []
        # nums.sort()

        # for idx, n in enumerate(nums):
        #     # if positive number break the loop bc wont add up to 0
        #     if n > 0:
        #         break

        #     # if duplicate value continue
        #     if idx > 0 and n== nums[idx-1]:
        #         continue

        #     left = idx + 1
        #     right = len(nums) - 1

        #     while left < right:
        #         three_sum = n + nums[left] + nums[right]

        #         if three_sum == 0:
        #             res.append([n, nums[left], nums[right]])
        #             left += 1
        #             right -= 1
        #             # skip past duplicates
        #             while nums[left] == nums[left - 1] and left < right:
        #                 left += 1
        #         elif three_sum > 0:
        #             right -= 1
        #         elif three_sum < 0:
        #             left += 1
                
        # return res
                
    # Time: O(n^2)
    # Space: O(1)


        





























