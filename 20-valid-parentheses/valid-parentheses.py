# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) == 1: return False

#         stack = []
#         for curr in s:
#             if curr == "(" or curr == "{" or curr == "[":
#                 stack.append(curr)
#             else:
#                 if len(stack) == 0: 
#                     return False
#                 matching_paren = stack.pop()
#                 if curr == ")" and matching_paren != "(":
#                     return False
#                 elif curr == "}" and matching_paren != "{":
#                     return False
#                 elif curr == "]" and matching_paren != "[":
#                     return False

#         return True if len(stack) == 0 else False


# neetcode soln 

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map: # c is an open parentheses 
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: # not an open parantheses and nothing to pop from stack
                return False
            stack.pop()

        return not stack










