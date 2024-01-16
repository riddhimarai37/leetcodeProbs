class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_map = {}
        res = 0

        l = 0
        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)

            # checking if current window is valid; if not shift
            # r-l+1 - max(char_map.values()) == number of replacement
            if (r-l+1) - max(char_map.values()) > k :
                char_map[s[l]] -= 1
                l += 1

            # max is size of the windwo or previous max
            res = max(res,r-l+1)

        return res