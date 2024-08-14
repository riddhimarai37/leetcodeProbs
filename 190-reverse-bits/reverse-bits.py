class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            bits = (n >> i) & 1
            ans += (bits << (31-i))
        return ans 
























        # ans = 0
        # for i in range(32):
        #     bit = (n >> i) & 1
        #     ans += (bit << (31 - i))
        # return ans
        