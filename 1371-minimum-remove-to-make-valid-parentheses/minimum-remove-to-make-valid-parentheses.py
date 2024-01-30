class Solution:
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

    def minRemoveToMakeValid(self, s:str) -> str:
        # pass 1: remove all invalid ")"
        string_builder =[]
        balance = 0

        for char in s:
            if char == "(":
                balance += 1
            if char == ")":
                if balance == 0:
                    continue
                balance -= 1
            string_builder.append(char)

        if balance == 0:
            return "".join(string_builder)

        # pass 2: remove all invalid "("
        res = []
        balance = 0

        for idx in range(len(string_builder)-1, -1, -1):
            if string_builder[idx] == "(":
                if balance == 0:
                    continue
                balance -= 1 
            elif string_builder[idx] == ")":
                balance += 1
            res.append(string_builder[idx])

        return "".join(reversed(res))                








        