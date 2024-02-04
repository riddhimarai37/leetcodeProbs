class Solution:
    # traverse the array from the right and keep track of the current max height 
    def findBuildings(self, heights: List[int]) -> List[int]:
        # max_height = 0
        # res = collections.deque([])

        # for i in range(len(heights) - 1, - 1, - 1):
        #     cur_height = heights[i]

        #     if cur_height > max_height:
        #         res.appendleft(i)
        #         max_height = cur_height

        # return res   

        # follow-up: just got a phone interview from Facebook. They asked this question, first  
        # part was to count how many buildings have an ocean view. The second part was iterate  #from the beginning and return the list of indexes. I used stack for the second part.

        res = []

        for i in range(len(heights)):
            cur_height = heights[i]
            while res and cur_height >= heights[res[-1]]:
                res.pop()
            res.append(i)
        return res

        
