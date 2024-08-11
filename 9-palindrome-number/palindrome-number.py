class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False

        if x < 10:
            return True

        reverse = 0 
        temp = x
        while temp > 0:
            reverse *= 10
            reverse += temp % 10
            temp //= 10

        return reverse == x
    

        