class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}
        for c in s: 
            count[c] = 1 + count.get(c,0)

        # max heap to keep track of characters with highest count
        max_heap = []
        for c in count: 
            max_heap.append([-count[c], c])

        heapq.heapify(max_heap) # o(nlogn)

        res = ''
        prev = None 

        while max_heap or prev: 
            # no more characters and still need to append
            if prev and not max_heap:
                return ''

            # update res and value
            count, char = heapq.heappop(max_heap)
            res += char
            count += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if count != 0:
                prev = [count,char]

        return res



            











        


        