class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        count = [[] for i in range(len(nums)+1)]

        for n in nums:
            num_count[n] = 1 + num_count.get(n,0)

        for n,c in num_count.items(): 
            count[c].append(n)

        res = []

        for i in range(len(count)-1,0,-1):
            if len(res) < k:
                for n in count[i]:
                    res.append(n)

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
            
            

        