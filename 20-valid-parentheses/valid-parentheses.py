class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False

        stack = []
        for curr in s:
            if curr == "(" or curr == "{" or curr == "[":
                stack.append(curr)
            else:
                if len(stack) == 0: 
                    return False
                matching_paren = stack.pop()
                if curr == ")" and matching_paren != "(":
                    return False
                elif curr == "}" and matching_paren != "{":
                    return False
                elif curr == "]" and matching_paren != "[":
                    return False

        return True if len(stack) == 0 else False

















        stack = []

        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                curr_char = stack.pop()

                if curr_char == "(":
                    if char != ")":
                        return False
                elif curr_char == "{":
                    if char != "}":
                        return False
                elif curr_char == "[":
                    if char != "]":
                        return False
        
        if stack:
            return False

        return True

        

