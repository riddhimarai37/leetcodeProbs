class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for idx, num in enumerate(nums):
            if num > 0:
                break

            if idx > 0 and num == nums[idx-1]:
                continue

            l = idx + 1
            r = len(nums) - 1

            while l < r:
                three_sum = num + nums[l] + nums[r]

                # if sum is positive
                if three_sum > 0:
                    r -= 1
                # if sum is negative
                elif three_sum < 0:
                    l += 1
                # if sum == 0
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return ans

                


        





























