class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # invalid window
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(r-l+1, res)

        return res
        
        
                









        



            
















        
        # count = {}
        # left = 0
        # res = 0

        # for right in range(len(s)):
        #     # increment right count
        #     count[s[right]] = 1 + count.get(s[right], 0)

        #     # checking if current window is valid
        #     while right-left+1 - max(count.values()) > k:
        #         count[s[left]] -= 1
        #         left += 1

        #     res = max(res, right - left + 1)

        # return res



        # O(n) or O(26 * n) time and O(1) space bc of char map













        
        # char_map = {}
        # res = 0

        # l = 0
        # for r in range(len(s)):
        #     char_map[s[r]] = 1 + char_map.get(s[r], 0)

        #     # checking if current window is valid; if not shift
        #     # r-l+1 - max(char_map.values()) == number of replacement
        #     if (r-l+1) - max(char_map.values()) > k :
        #         char_map[s[l]] -= 1
        #         l += 1

        #     # max is size of the windwo or previous max
        #     res = max(res,r-l+1)

        # return res