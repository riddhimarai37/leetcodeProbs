

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_counter = collections.Counter(s)
        res = ""

        for c in order:
            if c in s_counter.keys():
                res += c * s_counter[c]
                del s_counter[c]

        for c, count in s_counter.items():
            res += c * count
            
        return res
            



















        # count = {}
        # res = ""

        # for c in s:
        #     count[c] = 1 + count.get(c, 0)

        # for c in order:
        #     if c in count:
        #         res += c * count[c]
        #         del count[c]

        # for c in count:
        #     res += c * count[c]

        # return res
        
        


