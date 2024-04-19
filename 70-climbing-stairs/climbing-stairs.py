class Solution:
    def climbStairs(self, n: int) -> int:
        # edge case
        # if n <= 3:
        #     return n
        # n1, n2 = 2,3
        one,two = 1,1

        for i in range(n-1):
            temp = one 
            one = one + two
            two = temp

        return one
        
        