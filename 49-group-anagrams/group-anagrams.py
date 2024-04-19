class Solution:
    def groupAnagrams(self, strs):
        count_dicts = {}
        res = []

        for s in strs:
            count = [0] * 26 
            # populate the count dict
            for c in s:
                count[ord(c) - ord('a')] += 1

            if tuple(count) in count_dicts:
                count_dicts[tuple(count)].append(s)
            else:
                count_dicts[tuple(count)] = [s]

        for count in count_dicts:
            res.append(count_dicts[tuple(count)])

        return res
        
















        
        # anagram_map = defaultdict(list)
        
        # for word in strs:
        #     sorted_word = ''.join(sorted(word))
        #     anagram_map[sorted_word].append(word)
        
        # return anagram_map.values()
        # # O(m*nlogn)


# neetcode solution
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         ans = collections.defaultdict(list)

#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord("a")] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()

    # 0(mn) time complexity