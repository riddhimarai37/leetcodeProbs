# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(1):
            return 1

        # if isBadVersion(n) and not isBadVersion(n-1):
        #     return n

        
        l = 1
        r = n

        while l < r:
            mid = l + ((r-l) // 2)
            if isBadVersion(mid):
                r = mid
            elif isBadVersion(mid+1):
                return mid + 1
            else:
                l = mid

        

        

        