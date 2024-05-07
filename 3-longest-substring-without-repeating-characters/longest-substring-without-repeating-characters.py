class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0 
        res = 0 

        # right pointer increments every time
        for right in range(len(s)):
            # while we keep getting repeating chars in window, remove from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)

        return res


        # # O(n) time and space





    

            
















        
        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res

