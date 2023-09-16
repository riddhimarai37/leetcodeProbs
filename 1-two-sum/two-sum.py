class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for idx, num in enumerate(nums):
            if num in num_map:
                return [num_map[num], idx]
            
            num_map[target-num] = idx


        
        