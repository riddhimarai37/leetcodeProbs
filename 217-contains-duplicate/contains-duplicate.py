class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)

        return False















        
        # unique_nums = set()

        # for num in nums:
        #     if num in unique_nums:
        #         return True
        #     unique_nums.add(num)

        # return False

        # #Time O(n) Space O(n)