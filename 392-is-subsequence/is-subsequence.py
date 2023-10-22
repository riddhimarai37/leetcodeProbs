class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pt1 = 0
        pt2 = 0

        if s == "":
            return True

        while pt2 < len(t):
            if s[pt1] == t[pt2]:
                if pt1 == len(s) - 1:
                    return True
                pt1 += 1
            pt2 += 1

        return False