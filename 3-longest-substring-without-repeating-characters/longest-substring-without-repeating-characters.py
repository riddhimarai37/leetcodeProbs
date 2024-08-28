class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l,r = 0, 1
        char_set = set(s[l])
        max_length = 1
        curr_length = 1

        while r < len(s):
            if s[r] in char_set:
                while l != r:
                    if s[l] == s[r]:
                        l += 1
                        break
                    char_set.remove(s[l])
                    l += 1
                curr_length = (r-l) 
                char_set.remove(s[r])
            char_set.add(s[r])
            curr_length += 1
            max_length = max(max_length, curr_length)
            r += 1

        return max_length 
            
            

























        # char_set = set()
        # left = 0 
        # res = 0 

        # # right pointer increments every time
        # for right in range(len(s)):
        #     # while we keep getting repeating chars in window, remove from the left
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1
        #     char_set.add(s[right])
        #     res = max(res, right - left + 1)

        # return res


        # # # O(n) time and space





    

            
















        
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

