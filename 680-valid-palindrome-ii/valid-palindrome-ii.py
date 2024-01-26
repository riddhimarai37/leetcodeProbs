class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(new_str):
            if len(new_str) < 1: return True
            left = 0
            right = len(new_str) - 1

            while left < right:
                if new_str[left] != new_str[right]:
                    return False
                left += 1
                right -= 1
            
            return True

            if self.isPalindrome(s):
                return True

            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return isPalindrome(s[:left] + s[left+1:]) or isPalindrome(s[:right] + s[right+1:])
                left += 1
                right -= 1
            

        


        














        
        def isPalindrome(left, right):
            l = left
            r = right
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -=1 
            return True


        left = 0 
        right = len(s) - 1


        while left < right:
            if s[left] != s[right]:
                return isPalindrome(left + 1, right) or isPalindrome(left, right-1)
            left += 1
            right -= 1

        return True
        