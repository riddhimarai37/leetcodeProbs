# start at first digit of the num 
# store the digits in an array
# iterate through the array and find a digit larger than the current one 
# if found --> swap = True, keep track fo the indices and digits to swap 

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num
            
        digits = collections.deque([])

        while num:
            digits.appendleft(num % 10)
            num //= 10

        max_seen = -1
        max_seen_at = len(digits)


        # right to left pass to get largest digit
        i = len(digits) - 1

        while i >= 0:
            cur_num = digits[i]
            digits[i] = (cur_num, max_seen, max_seen_at)

            if cur_num > max_seen:
                max_seen = cur_num
                max_seen_at = i

            i -= 1

        # do the swap
        i = 0
        
        while i < len(digits):
            cur_num, max_to_right, max_seen_at = digits[i]
            if max_to_right > cur_num:
                # swap
                digits[i], digits[max_seen_at] = digits[max_seen_at], digits[i]
                break
            i += 1

        # turn list back into int

        res = 0
        for cur_num, _, _ in digits:
            res = res * 10 + cur_num

        return res




        