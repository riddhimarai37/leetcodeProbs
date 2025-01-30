class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target: 
                return mid

            # find sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target: 
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[r] >= target and nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid

        return -1
















        
        # low = 0 
        # high = len(nums) - 1

        # while low <= high:
        #     mid = low + (high-low) // 2
        #     if nums[mid] == target:
        #         return mid

        #     # left sorted portion
        #     if nums[low] <= nums[mid]:
        #         if target >= nums[low] and target <= nums[mid]:
        #             high = mid -1
        #         else:
        #             low = mid + 1
        #     # right sorted portion
        #     else:
        #         if target >= nums[mid] and target <= nums[high]:
        #             low = mid + 1
        #         else:
        #             high = mid -1

        # return -1

            

            
