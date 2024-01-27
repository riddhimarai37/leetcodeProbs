class Solution:
    def myPow(self, x: float, n: int) -> float:
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
        def binaryExp(x,n):
            if n == 0:
                return 1
            if n < 0:
                n = -n
                x = 1.0/x

            res = 1

            while n != 0:
                if n%2 == 1:
                    res *= x 
                    n -= 1
                x *= x
                n = n//2
            
            return res

        return binaryExp(x, float(n))
        









        

        
        