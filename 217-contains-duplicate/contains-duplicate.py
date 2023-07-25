class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for el in nums:
            if el not in num_dict:
                num_dict[el] = 1
            else:
                return True

        return False