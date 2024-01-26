class Solution:
    import re
    def calculate(self, s: str) -> int:
        idx = 0
        prev = curr = res = 0
        cur_oper = "+"

        # three cases 
        while idx < len(s):
            cur_char = s[idx]

            if cur_char.isdigit():
                while idx < len(s) and s[idx].isdigit():
                    curr = curr * 10 + int(s[idx]) # how get integer value of a string 
                    idx += 1
                idx -= 1 # go back to last valid char

                # apply previous operation
                if cur_oper == "+": 
                    res += curr
                    prev = curr
                elif cur_oper == "-":
                    res -= curr
                    prev = -curr
                elif cur_oper == "*":
                    res -= prev
                    res += prev * curr
                    prev = prev * curr
                else:
                    res -= prev
                    res += int(prev/curr) # for correct rounding purposes
                    prev = int(prev/curr)

                curr = 0
            elif cur_char != " ":
                cur_oper = cur_char

            idx += 1

        return res
        

            





            

        