class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        for idx,n in enumerate(nums):
            comp = target - n
            if comp in hash_set:
                return [idx, hash_set[comp]]
            hash_set[n] = idx

            

















        
        # num_map = {}

        # for idx,n in enumerate(nums):
        #     comp = target - n
        #     if comp in num_map:
        #         return [idx, num_map[comp]]
        #     num_map[n] = idx


        # Time: O(n) Space: O(n)

        
