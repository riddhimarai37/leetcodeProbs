class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        # populate array with prefix values
        for idx in range(0, len(res)):
            res[idx] = prefix
            prefix *= nums[idx]

        postfix = 1
        for idx in range(len(res) - 1, -1 ,-1):
            res[idx] *= postfix
            postfix *= nums[idx]

        return res





        




















        
        # ans = []
        # prefix_prod = 1
        # i = 0
        # j = len(nums) - 1

        # while i < len(nums):
        #     ans.append(prefix_prod)
        #     prefix_prod *= nums[i]
        #     i += 1


        # postfix_prod = 1

        # while j >= 0:
        #     ans[j] *= postfix_prod
        #     postfix_prod *= nums[j]
        #     j -= 1


        # return ans


        # Time: O(n) Space: O(1)
        
            



