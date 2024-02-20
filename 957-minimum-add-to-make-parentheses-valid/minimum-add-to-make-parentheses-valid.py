
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0 
        right = 0

        for c in s:
            if c == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right += 1

        return left + right




















        # ans = bal = 0

        # for c in s:
        #     if c == "(":
        #         bal += 1
        #     else:
        #         bal -= 1

        #     if bal == -1:
        #         ans += 1
        #         bal += 1

        # return ans + bal




        