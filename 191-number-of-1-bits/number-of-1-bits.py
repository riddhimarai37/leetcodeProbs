class Solution:
    def hammingWeight(self, n: int) -> int:
        hammingWeight = 0
        for c in bin(n)[2:]:
            if c == '1':
                hammingWeight += 1
        return hammingWeight

        