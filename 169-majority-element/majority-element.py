class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el_count = {}

        curr_max = 0
        curr_maj_el = 0
        for el in nums:
            if el not in el_count:
                el_count[el] = 1
            else:
                el_count[el] += 1
            curr_max = max(curr_max, el_count[el])
            if curr_max == el_count[el]:
                curr_maj_el = el

        return curr_maj_el

        

        # print(el_count)
        # curr_max = 1
        # curr_max_idx = 0
        # for curr in el_count:
        #     curr_max = max(curr_max,curr)
        #     if curr_max == curr:
        #         curr_max_idx = curr
        
        # return curr_max_idx
