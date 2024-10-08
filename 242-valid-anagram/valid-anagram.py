class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for idx in range(len(s)):
            s_dict[s[idx]] = 1 + s_dict.get(s[idx],0)
            t_dict[t[idx]] = 1 + t_dict.get(t[idx],0)

        return s_dict == t_dict



        





















        # if len(s) != len(t):
        #     return False


        # s_count = {}
        # t_count = {}

        # for idx in range(len(s)):
        #     s_count[s[idx]] = 1 + s_count.get(s[idx], 0)
        #     t_count[t[idx]] = 1 + t_count.get(t[idx],0)

        # return s_count == t_count


    # Time O(n) Space O(26) = O(1)






