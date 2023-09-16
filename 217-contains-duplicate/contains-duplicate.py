class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for el in nums:
            if el in hash_set:
                return True

            hash_set.add(el)

        return False


        # num_dict = {}

        # for el in nums:
        #     if el not in num_dict:
        #         num_dict[el] = 1
        #     else:
        #         return True

        # return False