class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res





















        # My Solution 
        # res = ""
        # min_length = 200

        # for s in strs:
        #     min_length = min(min_length, len(s))
        #     if len(s) == min_length:
        #         res = s

        # for s in strs:
        #     if s == res:
        #         continue
        #     i = 0
        #     while i < min_length:
        #         if s[i] != res[i]:
        #             res = res[:i]
        #             min_length = len(res)
        #             break
        #         i += 1

        # return res

        



        