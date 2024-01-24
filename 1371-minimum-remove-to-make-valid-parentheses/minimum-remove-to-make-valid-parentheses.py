class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 1 and (s[0] == "(" or s[0] == ")"):
            return ""
        elif len(s)==1:
            return s

        stack = []
        res = ""

        for idx,c in enumerate(s):
            if c == "(":
                stack.append((idx,c))
            elif c == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append((idx,c))

        while stack:
            idx = stack.pop()[0]
            s = s[:idx] + s[idx+1:]   

        return s


        