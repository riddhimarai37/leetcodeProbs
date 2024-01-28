class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = 0
        ptr = len(heights) - 1
        res = []

        while ptr >= 0:
            if heights[ptr] > max_height:
                res.append(ptr)
                max_height = heights[ptr]
            ptr -= 1
            
        res.reverse()
        return res