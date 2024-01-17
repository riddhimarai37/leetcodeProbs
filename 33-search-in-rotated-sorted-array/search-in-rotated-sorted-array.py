# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums) == 1 and nums[0] == target: 
#             return 0
#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             mid = left + (right-left) // 2

#             if nums[mid] == target:
#                 return mid
#             elif nums[left] == target:
#                 return left
#             elif nums[right] == target:
#                 return right

#             if nums[left] < nums[mid]:
#                 if nums[left] < target < nums[mid]:
#                     right = mid - 1
#                     continue
#                 else:
#                     left = mid + 1
#                     continue
#             else:
#                 if nums[mid] < target < nums[right]:
#                     left = mid + 1
#                     continue
#                 else:
#                     right = mid - 1
#                     continue

#         return -1
        


        # neetcode (cleaner solution)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1



