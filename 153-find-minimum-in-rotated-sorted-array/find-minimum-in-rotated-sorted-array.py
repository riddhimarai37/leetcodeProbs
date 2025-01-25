class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r-l)//2

            if nums[l] < nums[r]:
                return nums[l]

            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
    














