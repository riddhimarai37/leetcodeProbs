class SparseVector:
    def __init__(self, nums: List[int]):
        self.new_nums = []
        for idx, n in enumerate(nums):
            if n != 0:
                self.new_nums.append((n, idx))


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        pt1 = pt2 = 0
        dot_prod = 0
        
        while pt1 < len(self.new_nums) and pt2 < len(vec.new_nums):
            n1, idx1 = self.new_nums[pt1]
            n2, idx2 = vec.new_nums[pt2]

            if idx1 == idx2:
                dot_prod += n1 * n2
                pt1 += 1
                pt2 += 1
            elif idx1 > idx2:
                pt2 += 1
            elif idx2 > idx1:
                pt1 += 1

        return dot_prod
            























    # def __init__(self, nums: List[int]):
        # self.values = []
        # for i,n in enumerate(nums):
        #     if n != 0:
        #         self.values.append((i,n))
    

    # Return the dotProduct of two sparse vectors
    # def dotProduct(self, vec: 'SparseVector') -> int:
        # dot_prod = 0
        # pt1 = pt2 = 0

        # while pt1 < len(self.values) and pt2 < len(vec.values):
        #     i, num1 = self.values[pt1]
        #     j, num2 = vec.values[pt2]

        #     if i == j:
        #         dot_prod += num1 * num2 
        #         pt1 += 1
        #         pt2 += 1
        #     elif i > j:
        #         pt2 += 1
        #     else:
        #         pt1 += 1

        # return dot_prod
            

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

