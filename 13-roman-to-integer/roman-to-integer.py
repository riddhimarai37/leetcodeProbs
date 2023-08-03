class Solution:
    def romanToInt(self, s: str) -> int:
         roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
         n = len(s)

         if n == 1:
            return roman_map[s]

         left = 0
         right = 1

         curr_sum = 0

         while left < n:
            # if last char hasn't been added
            if right >= n:
               curr_sum += roman_map[s[left]]
               left += 1
               break
            # dealing with subtraction cases
            if s[left] == 'I':
               if s[right] == 'V':
                  curr_sum += 4 
                  left += 2
                  right += 2
               elif s[right] == 'X':
                  curr_sum += 9
                  left += 2
                  right += 2
               else:
                  curr_sum += 1
                  left += 1 
                  right += 1
            elif s[left] == 'X':
               if s[right] == 'L':
                  curr_sum += 40 
                  left += 2
                  right += 2
               elif s[right] == 'C':
                  curr_sum += 90
                  left += 2
                  right += 2
               else:
                  curr_sum += 10
                  left += 1
                  right += 1
            elif s[left] == 'C':
               if s[right] == 'D':
                  curr_sum += 400 
                  left += 2
                  right += 2
               elif s[right] == 'M':
                  curr_sum += 900
                  left += 2
                  right += 2
               else:
                  curr_sum += 100
                  left += 1
                  right += 1
            else:
               curr_sum += roman_map[s[left]]
               left += 1
               right += 1

         return curr_sum
         
            



