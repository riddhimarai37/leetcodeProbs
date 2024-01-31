# example:
#  [[1,3], [-2,2]] heap: [1,3]

import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap  = []

        for cur in points:
            # calculate distance from zero 
            pow_val = math.pow(-cur[0],2) + math.pow(-cur[1],2)
            dist  = math.sqrt(pow_val)
            if len(heap) < k:
                heapq.heappush(heap,[-1*dist,cur[0], cur[1]])
            else:
                heapq.heappushpop(heap, [-1*dist, cur[0],cur[1]])

        res = []
        for dist,row,col in heap:
            res.append([row,col])

        return res



        