class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return x
        # elif n == -1:
        #     return 1/x
            
        # result = self.myPow(x,n//2)
        # return result * result * self.myPow(x,n%2)


        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f





        

        
        