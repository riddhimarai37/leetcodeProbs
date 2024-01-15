class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for curr in nums:
            if curr in numSet:
                return True
            numSet.add(curr)

        return False
