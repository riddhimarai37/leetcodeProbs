class Solution:
    def groupAnagrams(self, strs):
        res_dict = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            count = tuple(count)
            if count in res_dict:
                res_dict[count].append(s)
            else:
                res_dict[count] = [s]

        return res_dict.values()

















        
    


# neetcode solution
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = collections.defaultdict(list)

#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
                    #unique tuple 
#             ans[tuple(count)].append(s)
#         return ans.values()

    # 0(mn) time complexity