class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}

        for idx in range(len(nums)):
            comp = target - nums[idx]

            if comp in num_map:
                return [idx, num_map[comp]]
            
            num_map[nums[idx]] = idx


        
        