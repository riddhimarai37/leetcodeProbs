class SparseVector:
    def __init__(self, nums: List[int]):
        self.mult_values = []
        for idx,n in enumerate(nums):
            if n != 0:
                self.mult_values.append((n, idx))
    

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        pt1 = pt2 = 0
        res = 0

        while pt1 < len(self.mult_values) and pt2 < len(vec.mult_values):
            # if indices are equal add the dot product to 0
            idx1 = self.mult_values[pt1][1]
            idx2 = vec.mult_values[pt2][1]
            if idx1 == idx2:
                res += self.mult_values[pt1][0] * vec.mult_values[pt2][0]
                pt1 += 1
                pt2 += 1
            elif idx1 > idx2:
                pt2 +=1
            else:
                pt1 += 1

        return res
                

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)