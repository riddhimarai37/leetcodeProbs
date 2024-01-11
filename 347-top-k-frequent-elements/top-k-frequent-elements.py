class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        if len(nums) == k:
            return nums

        num_freq = {}
        for curr in nums:
            num_freq[curr] = 1 + num_freq.get(curr, 0)

        num_freq = sorted(num_freq.items(), key=lambda x: x[1], reverse=True)
        print(num_freq)
        
        for i in range(0, k):
            results.append(num_freq[i][0])

        return results

