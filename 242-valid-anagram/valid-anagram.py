class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        length = len(s)
        s_map = {}
        t_map = {}

        for i in range(length):
            s_map[s[i]] = s_map.get(s[i],0) + 1
            t_map[t[i]] = t_map.get(t[i],0) + 1

        return s_map == t_map




















        # if len(s) != len(t):
        #     return False


        # s_count = {}
        # t_count = {}

        # for idx in range(len(s)):
        #     s_count[s[idx]] = 1 + s_count.get(s[idx], 0)
        #     t_count[t[idx]] = 1 + t_count.get(t[idx],0)

        # return s_count == t_count


    # Time O(n) Space O(26) = O(1)






