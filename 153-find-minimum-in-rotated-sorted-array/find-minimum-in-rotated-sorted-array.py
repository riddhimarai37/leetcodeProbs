class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            if nums[low] < nums[high]:
                return nums[low]

            mid = low + (high-low) // 2

            if nums[mid] < nums[low]:
                high = mid 
            elif nums[mid] > nums[high]:
                low = mid + 1

        return nums[low]

        