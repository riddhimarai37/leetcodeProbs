class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[left] != " " and s[right].isalnum() and s[right] != " ":
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            elif s[left] == " " or not s[left].isalnum():
                left += 1
            elif s[right] == " " or not s[right].isalnum():
                right -= 1

        return True


                



















        # s = s.lower()
        # left = 0 
        # right = len(s) - 1

        # while left < right:
        #     if s[left].isalnum() and s[right].isalnum() and s[left] != s[right]:
        #         return False
        #     elif not s[left].isalnum():
        #         left += 1
        #     elif not s[right].isalnum():
        #         right -= 1
        #     else:
        #         left += 1
        #         right -= 1

        # return True


        # Time O(n) Space: O(1)
            

            

            









# # neetcode solution # 1 -- uses extra space

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new = ''
#         for a in s:
#             if a.isalpha() or a.isdigit():
#                 new += a.lower()
#         return (new == new[::-1])

# # neetcode solution #2 -- uses less space but a little less efficient

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left = 0
#         right = len(s) - 1

#         while left < right:
#             while left < right and not self.alphaNum(s[left]):
#                 left += 1
#             while right > left and not self.alphaNum(s[right]) :
#                 right -= 1

#             if s[left].lower() != s[right].lower():
#                 return False

#             left += 1
#             right -=1

#         return True



#     def alphaNum(self, c) -> bool:
#         return ((ord('a') <= ord(c) <= ord('z')) or
#                 (ord('A') <= ord(c) <= ord('Z')) or 
#                 (ord('0') <= ord(c) <= ord('9')))
