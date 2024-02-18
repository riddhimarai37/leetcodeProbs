class Solution:
    def __init__(self, w: List[int]):
        self.total_sum = 0
        self.pref_sums = []
        for weight in w:
            self.total_sum += weight
            self.pref_sums.append(self.total_sum)

    def pickIndex(self) -> int:
        rand_num = random.random() * self.total_sum

        left = 0
        right = len(self.pref_sums) - 1

        while left < right:
            mid = left + (right-left)//2
            if rand_num > self.pref_sums[mid]:
                left = mid + 1
            else:
                right = mid
        
        return left




















    # def __init__(self, w: List[int]):
    #     self.sums = []
    #     self.prefix_sum = 0
    #     for weight in w:
    #         self.prefix_sum += weight
    #         self.sums.append(self.prefix_sum)

    # def pickIndex(self) -> int:
    #     if len(self.sums) == 1:
    #         return 0

    #     target = random.random() * self.prefix_sum
    #     # perform binary search to find where target falls
    #     low = 0
    #     high = len(self.sums)
    #     while low < high:
    #         mid = low + (high-low) // 2
    #         if target > self.sums[mid]:
    #             low = mid + 1
    #         else:
    #             high = mid
    #     return low



    # Constructor Time = O(N), PickIndex Time = O(logN)
    # Constructor Space = O(N), PickIndex Space = O(1)

    

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

    