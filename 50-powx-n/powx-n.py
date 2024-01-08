class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
            
        result = self.myPow(x,n//2)
        return result * result * self.myPow(x,n%2)






        

        
        