class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_nums = set()

        for curr in nums:
            if curr not in distinct_nums:
                distinct_nums.add(curr)

        return False if len(nums) == len(distinct_nums) else True


        nums = [1,2,3,1]
        print(containsDuplicate(self,nums))

        nums = [1,2,3]
        print(containsDuplicate(self,nums))
    
        nums = [3]
        print(containsDuplicate(self,nums))

