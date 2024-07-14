class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        low = 0 
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low)//2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1 


















        
        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = left + ((right - left)//2)

        #     if nums[mid] > target:
        #         right = mid - 1
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         return mid

        # return -1

        

        # Time: O(logn) Space: O(1)