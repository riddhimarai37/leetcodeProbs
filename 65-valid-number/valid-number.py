class Solution:
    def isNumber(self, s: str) -> bool:

        def isInteger(curr_str):
            if not curr_str:
                return False

            seenDigit = False
            idx = 0
            
            if curr_str[0] in ['+', '-']:
                idx += 1

            while idx < len(curr_str):
                curr_char = curr_str[idx]
                if curr_char.isdigit():
                    seenDigit = True
                else:
                    return False
                idx += 1

            return seenDigit


        seenDigit, seenDot = False, False

        idx = 0
        if s[idx] == '+' or s[idx] == '-':
            idx += 1

        while idx < len(s):
            curr_char = s[idx]
            if curr_char.isalpha():
                if curr_char not in ['e', 'E']:
                    return False
                else:
                    return seenDigit and isInteger(s[idx+1:])
            elif curr_char == ".":
                if seenDot:
                    return False
                else:
                    seenDot = True
            elif curr_char in ['+', '-']:
                    return False
            else:
                seenDigit = True
            idx +=1

        return seenDigit

                    