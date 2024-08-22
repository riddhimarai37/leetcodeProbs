class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x,y = p[0],p[1]
            dist = -(x*x + y*y)
        
            if len(heap) <  k:
                heapq.heappush(heap, [dist, x,y])
            else:
                if heap[0][0] < dist:
                    heapq.heappop(heap)
                    heapq.heappush(heap,[dist,x,y])


        return [(x,y) for (dist, x, y) in heap]