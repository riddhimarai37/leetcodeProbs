class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx, num in enumerate(nums):
            comp = target - num
            if comp in hash_map:
                return [idx, hash_map[comp]]
            hash_map[num] = idx

        














        
        # num_map = {}

        # for idx,n in enumerate(nums):
        #     comp = target - n
        #     if comp in num_map:
        #         return [idx, num_map[comp]]
        #     num_map[n] = idx


        # Time: O(n) Space: O(n)

        
