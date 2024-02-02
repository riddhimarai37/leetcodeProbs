
# iterate through order 
# check if the curr char occurs in s at all
# if true: add that char to result 

# iterate through s:
# if the current char is in res: skip 
# else: add it to res 


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = {}
        res = ""

        for c in s:
            count[c] = 1 + count.get(c, 0)

        for c in order:
            if c in count:
                res += c * count[c]
                del count[c]

        for c in count:
            res += c * count[c]

        return res
        
        


