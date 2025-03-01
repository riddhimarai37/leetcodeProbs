class Solution:
    def groupAnagrams(self, strs):
        hash_map = collections.defaultdict(list)

        for s in strs: 
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            hash_map[tuple(count)].append(s)


        res = []

        for curr in hash_map:
            res.append(hash_map[curr])

        return res


            














        
    


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