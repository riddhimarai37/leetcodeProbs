class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        pref_sum = 0
 
        for weight in w:
            pref_sum += weight
            self.prefix_sums.append(pref_sum)
        self.total_sum = pref_sum

    def pickIndex(self) -> int:
        rand_val = self.total_sum * random.random()
        # run a binary search to find the target zone
        low = 0
        high = len(self.prefix_sums)

        while low < high:
            mid = low + (high-low) // 2
            if rand_val > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid

        return low


    # Constructor Time = O(N), PickIndex Time = O(logN)
    # Constructor Space = O(N), PickIndex Space = O(1)


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()