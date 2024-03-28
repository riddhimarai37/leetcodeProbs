class Solution:
    def countBits(self, n: int) -> List[int]:
        #DP solution
        dp = [0] * (n+1)
        offset = 1

        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp




























        # brute force 
        # ans = []
        # idx = 0

        # while idx <= n:
        #     curr_num = idx
        #     num_of_ones = 0

        #     while curr_num:
        #         if curr_num % 2 == 1:
        #             num_of_ones += 1
        #         curr_num = curr_num >> 1

        #     ans.append(num_of_ones)
        #     idx += 1
    
        # return ans

        # Time O(nlogn)



        