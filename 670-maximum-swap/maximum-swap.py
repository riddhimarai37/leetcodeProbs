

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num <= 11:
            return num

        # create num_arr

        num_arr = collections.deque([])

        while num:
            num_arr.appendleft(num % 10)
            num //= 10

        # find max to the right of every digit
        max_digit = -1
        max_idx = len(num_arr)
        i = len(num_arr) - 1

        while i >= 0:
            curr_digit = num_arr[i]
            num_arr[i] = (curr_digit, max_digit, max_idx)

            if curr_digit > max_digit:
                max_digit = curr_digit
                max_idx = i

            i -= 1

        i = 0

        while i < len(num_arr):
            curr_digit, max_to_right, max_idx_right = num_arr[i]

            if max_to_right > curr_digit:
                num_arr[i], num_arr[max_idx_right] = num_arr[max_idx_right], num_arr[i]
                break

            i += 1

        res = 0

        for digit,_,_ in num_arr:
            res = res * 10 + digit

        return res





            



     
            
            

    # time: O(N) space: O(N)












        # if num <= 11:
        #     return num
            
        # digits = collections.deque([])

        # while num:
        #     digits.appendleft(num % 10)
        #     num //= 10

        # max_seen = -1
        # max_seen_at = len(digits)

        # # right to left pass to get largest digit
        # i = len(digits) - 1

        # while i >= 0:
        #     cur_num = digits[i]
        #     digits[i] = (cur_num, max_seen, max_seen_at)

        #     if cur_num > max_seen:
        #         max_seen = cur_num
        #         max_seen_at = i

        #     i -= 1

        # # do the swap
        # i = 0
        
        # while i < len(digits):
        #     cur_num, max_to_right, max_seen_at = digits[i]
        #     if max_to_right > cur_num:
        #         # swap
        #         digits[i], digits[max_seen_at] = digits[max_seen_at], digits[i]
        #         break
        #     i += 1

        # # turn list back into int

        # res = 0
        # for cur_num, _, _ in digits:
        #     res = res * 10 + cur_num

        # return res




        