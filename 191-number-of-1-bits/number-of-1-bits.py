class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            # see if last bit is 1
            if n % 2 == 1:
                res += 1
            # move n down 1 bit
            n = n >> 1
        return res

        