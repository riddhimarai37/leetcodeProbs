class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        res = 0

        for c in s:
            counter[c] = 1 + counter.get(c,0)
            if counter[c] % 2 == 0:
                res += 2

        for c in counter.values():
            if c % 2 == 1:
                res += 1
                break

        return res

        