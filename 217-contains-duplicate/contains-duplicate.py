class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for el in nums:
            if el not in hash_set:
                hash_set.add(el)
            else:
                return True

        return False


        # num_dict = {}

        # for el in nums:
        #     if el not in num_dict:
        #         num_dict[el] = 1
        #     else:
        #         return True

        # return False