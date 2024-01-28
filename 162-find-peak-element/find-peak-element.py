class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 
        left = 0 
        right = len(nums) - 1

        while left < right:
            if left == 0 and nums[left] > nums[left+1]:
                return left
            if right == len(nums) - 1 and nums[right] > nums[right-1]:
                return right

            mid = left + (right-left) // 2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid+1] > nums[mid]:
                left = mid
            else:
                right = mid

            


        