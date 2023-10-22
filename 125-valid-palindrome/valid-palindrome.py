class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        s = s.lower()

        while left < right:
            # check for invalid characters
            while left < right and s[left].isalnum() == False:
                left += 1
            while left < right and s[right].isalnum() == False:
                right -= 1

            if left > right or s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True