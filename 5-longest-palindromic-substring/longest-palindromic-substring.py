# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         res = ""
#         longest = 0


#         for idx in range(len(s)):
#             # res is odd length
#             left = idx
#             right = idx

#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 if (right - left + 1) > longest:
#                     res = s[left:right+1]
#                     longest = right - left + 1
#                 left -= 1
#                 right += 1


#             # res is even length
#             left = idx
#             right = idx + 1

#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 if (right - left + 1) > longest:
#                     res = s[left:right+1]
#                     longest = right - left + 1
#                 left -= 1
#                 right -= 1

#         return res


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res


                

            

