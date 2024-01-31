class Solution:
    
    def dfs(self, s, depth, l, r, l_rmv, r_rmv, new_s):
        if l_rmv < 0 or r_rmv < 0 or r > l:
            return
        if depth == len(s):
            if l == r and l_rmv == 0 and r_rmv == 0:
                self.ans.add(new_s)
        else:
            is_open, is_close = s[depth] == '(', s[depth] == ')'
            self.dfs(s, depth + 1, l + is_open, r + is_close, l_rmv, r_rmv, new_s + s[depth])
            if is_open or is_close:
                self.dfs(s, depth + 1, l, r, l_rmv - is_open, r_rmv - is_close, new_s)
    
    def removeInvalidParentheses(self, s: str) -> List[str]:        
        left, right = 0, 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1
        self.ans = set()
        self.dfs(s, 0, 0, 0, left, right, "")
        return list(self.ans)