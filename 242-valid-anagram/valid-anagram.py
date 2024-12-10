class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        t_count = [0] * 26

        for c in s:
            s_count[ord(c) - ord('a')] += 1

        for c in t:
            t_count[ord(c) - ord('a')] += 1


        return s_count == t_count



        





















        # if len(s) != len(t):
        #     return False


        # s_count = {}
        # t_count = {}

        # for idx in range(len(s)):
        #     s_count[s[idx]] = 1 + s_count.get(s[idx], 0)
        #     t_count[t[idx]] = 1 + t_count.get(t[idx],0)

        # return s_count == t_count


    # Time O(n) Space O(26) = O(1)






