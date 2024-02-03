# left and right variables 
# res = ""
# first pass of s
# if curr c is: res += c
# if "(" --> add to res; left++ 
# if ")" --> left < right == 1: add to res; --> right += 1

# second pass of res
# if curr char ==> move forward
# if ")" --> move forward; right++
# if "(" --> right > left: add to res

class Solution:
    def minRemoveToMakeValid(self, s:str) -> str:
        left = right = 0
        string_builder = []

        # first pass 
        for c in s:
            if c.isalpha():
                string_builder.append(c)
            elif c == "(":
                string_builder.append(c)
                left += 1
            else:
                if left > right:
                    string_builder.append(c)
                    right += 1

        # second pass 
        res = []
        left = right = 0
        for idx in range(len(string_builder) - 1, -1, -1):
            cur_char = string_builder[idx]
            if cur_char.isalpha():
                res.append(cur_char)
            elif cur_char == ")":
                right += 1
                res.append(cur_char)
            else:
                if right > left:
                    res.append("(")
                    left += 1
                else:
                    continue

        return "".join(reversed(res))



    # def minRemoveToMakeValid(self, s: str) -> str:
    #     # stack approach
    #     if len(s) == 1 and (s[0] == "(" or s[0] == ")"):
    #         return ""
    #     elif len(s)==1:
    #         return s

    #     stack = []
    #     res = ""

    #     for idx,c in enumerate(s):
    #         if c == "(":
    #             stack.append((idx,c))
    #         elif c == ")":
    #             if stack and stack[-1][1] == "(":
    #                 stack.pop()
    #             else:
    #                 stack.append((idx,c))

    #     while stack:
    #         idx = stack.pop()[0]
    #         s = s[:idx] + s[idx+1:]   

    #     return s


    # two pass approach

    # def minRemoveToMakeValid(self, s:str) -> str:
    #     # pass 1: remove all invalid ")"
    #     string_builder =[]
    #     balance = 0

    #     for char in s:
    #         if char == "(":
    #             balance += 1
    #         if char == ")":
    #             if balance == 0:
    #                 continue
    #             balance -= 1
    #         string_builder.append(char)

    #     if balance == 0:
    #         return "".join(string_builder)

    #     # pass 2: remove all invalid "("
    #     res = []
    #     balance = 0

    #     for idx in range(len(string_builder)-1, -1, -1):
    #         if string_builder[idx] == "(":
    #             if balance == 0:
    #                 continue
    #             balance -= 1 
    #         elif string_builder[idx] == ")":
    #             balance += 1
    #         res.append(string_builder[idx])

    #     return "".join(reversed(res))                








        