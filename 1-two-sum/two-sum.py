class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for idx,n in enumerate(nums):
            comp = target - n 
            if comp in num_dict:
                return [idx, num_dict[comp]]

            num_dict[n] = idx















        
        # num_map = {}

        # for idx,n in enumerate(nums):
        #     comp = target - n
        #     if comp in num_map:
        #         return [idx, num_map[comp]]
        #     num_map[n] = idx


        # Time: O(n) Space: O(n)

        
