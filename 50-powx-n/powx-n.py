class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(num, power):
            if power == 0:
                return 1
            if power < 0:
                power = -power
                num = 1.0/num

            res = 1

            while power != 0:
                if power % 2 == 1:
                    res *= num 
                    power -= 1
                num *= num
                power //= 2
            
            return res

        return helper(x, float(n))
                

                

                
            





























        # if n == 0:
        #     return 1
        # elif n < 0:
        #     return 1.0/self.myPow(x, -n)
       
        # if n%2 == 1:
        #     return x * self.myPow(x*x, (n-1) // 2)
        # else:
        #     return self.myPow(x*x, n//2)

        # TIME: O(logn) SPACE: O(logn)


        # OPT APPROACH (binary exponentiation)
        # def binaryExp(x,n):
        #     if n == 0:
        #         return 1
        #     if n < 0:
        #         n = -n
        #         x = 1.0/x

        #     res = 1

        #     while n != 0:
        #         if n%2 == 1:
        #             res *= x 
        #             n -= 1
        #         x *= x
        #         n = n//2
            
        #     return res

        # return binaryExp(x, float(n))

        # # TIME O(logN) SPACE O(1)
        









        

        
        