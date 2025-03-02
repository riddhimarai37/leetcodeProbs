class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        if k == 0:
            return 0
        
        # max heap 
        max_heap = []

        for i in range(n):
            size = limits[i]
            # min heap
            min_heap = []
            
            if size != 0:
                for num in grid[i]:
                    if len(min_heap) < size:
                        heapq.heappush(min_heap, num)
                    else:
                        if min_heap[0] < num:
                            heapq.heappop(min_heap)
                            heapq.heappush(min_heap, num)

            while min_heap:
              val = heapq.heappop(min_heap)
              heapq.heappush(max_heap, -val)

        max_sum = 0
        cnt = 0
        while max_heap:
            val = -heapq.heappop(max_heap)
            max_sum += val
            cnt += 1

            if cnt == k:
                break

        return max_sum

        
        

            
            



        