class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                if n > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, n)

        return heap[0]



















        # heap = []

        # for n in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap, n)
        #     else:
        #         if n > heap[0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap,n)
                
        # return heapq.heappop(heap)

        # heap = nums[:k]
        # heapq.heapify(heap)
        
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        
        # return heap[0]