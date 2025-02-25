class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for idx,n in enumerate(nums):
            comp = target - n
            if comp in num_map:
                return [num_map[comp], idx]
            num_map[n] = idx
        
        
            


        




















        
        # num_map = {}

        # for idx,n in enumerate(nums):
        #     comp = target - n
        #     if comp in num_map:
        #         return [idx, num_map[comp]]
        #     num_map[n] = idx


        # Time: O(n) Space: O(n)

        
