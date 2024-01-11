class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        s_counter = {}
        t_counter = {}  
        idx = 0

        def increment_or_add(idx, str, counter):
            if str[idx] in counter: 
                counter[str[idx]] += 1
            else: 
                counter[str[idx]] = 0

                
        while idx < len(s):
            increment_or_add(idx, s, s_counter)
            increment_or_add(idx, t, t_counter)
            idx += 1

        return True if s_counter == t_counter else False



        