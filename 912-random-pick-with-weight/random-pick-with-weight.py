class Solution:

    def __init__(self, w: List[int]):
        self.sums = []
        self.prefix_sum = 0
        for weight in w:
            self.prefix_sum += weight
            self.sums.append(self.prefix_sum)

    def pickIndex(self) -> int:
        if len(self.sums) == 1:
            return 0

        target = random.random() * self.prefix_sum
        # perform binary search to find where target falls
        low = 0
        high = len(self.sums)
        while low < high:
            mid = low + (high-low) // 2
            if target > self.sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low



    # Constructor Time = O(N), PickIndex Time = O(logN)
    # Constructor Space = O(N), PickIndex Space = O(1)

        # self.prefix_sums = []
        # pref_sum = 0
 
        # for weight in w:
        #     pref_sum += weight
        #     self.prefix_sums.append(pref_sum)
        # self.total_sum = pref_sum



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

        # rand_val = self.total_sum * random.random()
        # # run a binary search to find the target zone
        # low = 0
        # high = len(self.prefix_sums)

        # while low < high:
        #     mid = low + (high-low) // 2
        #     if rand_val > self.prefix_sums[mid]:
        #         low = mid + 1
        #     else:
        #         high = mid

        # return low