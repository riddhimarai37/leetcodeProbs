class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for idx,num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [idx, num_map[comp]]
            num_map[num] = idx
