class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest_string = -1
        self.res = set()

        self.dfs(s, 0, [], 0, 0)
        return self.res

    # dfs backtracking 

    def dfs(self, string, cur_idx, cur_res, left_count, right_count):
        if cur_idx >= len(string):
            if left_count == right_count:
                if len(cur_res) > self.longest_string:
                    self.longest_string = len(cur_res)
                    # reset 
                    self.res = set()
                    self.res.add("".join(cur_res))
                elif len(cur_res) == self.longest_string:
                    self.res.add("".join(cur_res))
        else:
            cur_char = string[cur_idx]

            if cur_char == "(":
                    # don't know if ")" exists later so must include this char
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, left_count + 1, right_count)
                cur_res.pop() # remove this char from current string

                    # testing string without this char
                self.dfs(string, cur_idx + 1, cur_res, left_count, right_count)
            elif cur_char == ")":
                    # run dfs with including this char and skipping it to see what's valid
                self.dfs(string, cur_idx + 1, cur_res, left_count, right_count)

                    # now testing including this char
                if left_count > right_count:
                        # including if we need another right paren
                    cur_res.append(cur_char)
                    self.dfs(string, cur_idx + 1, cur_res, left_count, right_count + 1)
                    cur_res.pop()
            else:
                    # any other character
                cur_res.append(cur_char)
                self.dfs(string, cur_idx + 1, cur_res, left_count, right_count)
                cur_res.pop()
