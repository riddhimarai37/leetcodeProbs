class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums = [lower-1] + nums + [upper+1]
        results = []

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                results.append([nums[i]+1, nums[i]+1])
            elif nums[i+1] - nums[i]>2:
                results.append([nums[i]+1, nums[i+1]-1])

        return results

                
            
            




        


        