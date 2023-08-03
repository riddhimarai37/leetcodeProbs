class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False

        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        for el in s:
            if el in opening:
                stack.append(el)
            else:
                if not stack:
                    return False
                curr_char = stack.pop()
                curr_char_idx = opening.index(curr_char)
                if curr_char_idx != closing.index(el):
                    return False
        
        if len(stack) != 0:
            return False

        return True

        

