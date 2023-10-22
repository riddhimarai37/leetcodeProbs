class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        s = ""
        idx = len(words) - 1

        while idx >= 0:
            s += words[idx] + ' '
            idx -= 1

        return s[0:len(s)-1]