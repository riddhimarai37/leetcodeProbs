class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix_prod = 1
        i = 0
        j = len(nums) - 1

        while i < len(nums):
            ans.append(prefix_prod)
            prefix_prod *= nums[i]
            i += 1


        postfix_prod = 1

        while j >= 0:
            ans[j] *= postfix_prod
            postfix_prod *= nums[j]
            j -= 1


        return ans














        
        # ans = []
        # prefix = nums[0]
        # idx = 1
        # ans.append(1)

        # while idx < len(nums):
        #     ans.append(prefix)
        #     prefix *= nums[idx]
        #     idx += 1

        # postfix = nums[-1]
        # idx = len(nums) - 2

        # while idx >= 0:
        #     ans[idx] *= postfix
        #     postfix *= nums[idx]
        #     idx -= 1

        # return ans


        # Time: O(n) Space: O(1)
        
            



