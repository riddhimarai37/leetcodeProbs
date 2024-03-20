class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for idx,num in enumerate(nums):
            comp = target - num
            if comp in dic:
                return [idx, dic[comp]]
            dic[num] = idx

        












        
        # num_map = {}

        # for idx,n in enumerate(nums):
        #     comp = target - n
        #     if comp in num_map:
        #         return [idx, num_map[comp]]
        #     num_map[n] = idx


        # Time: O(n) Space: O(n)

        
