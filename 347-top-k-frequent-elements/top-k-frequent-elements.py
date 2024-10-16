class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            counts[n] = 1 + counts.get(n,0)

        for n,c in counts.items():
            freq[c].append(n)

        idx = len(freq) - 1

        while len(res) < k:
            if len(freq[idx]) > 0:
                for n in freq[idx]:
                    res.append(n)
            idx -= 1

        return res

        
            






















        
        # count_dict = {}
        # res = []
        # count = [[] for i in range(len(nums) + 1)]

        # for n in nums:
        #     count_dict[n] = 1 + count_dict.get(n,0)

        # for n,c in count_dict.items():
        #     count[c].append(n)

        # for i in range(len(count)-1,0,-1):
        #     for n in count[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        # return res

        # Space: O(n) Time: O(n)
            
            

        