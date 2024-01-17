class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minVal = float("infinity")

        while left < right:
            mid = left + (right-left) // 2
            minVal = min(minVal, nums[mid])
            # min is in second half of array
            if nums[right] < nums[mid]:
                left = mid + 1
            # min is in first half of array
            else:
                right = mid - 1

        return min(minVal, nums[left])


        