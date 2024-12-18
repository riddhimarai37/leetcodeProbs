class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for s in strs: 
            # populate our count array
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagram_map[tuple(count)].append(s)

        return list(anagram_map.values())

            














        
    


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