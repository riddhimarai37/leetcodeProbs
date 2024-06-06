class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left = 0 
        right = len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid 

        return -1

        