class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_n1 = m - 1
        last_n2 = n - 1
        curr_pt = m + n - 1

        while last_n2 >= 0:
            if last_n1 >= 0 and nums1[last_n1] > nums2[last_n2]:
                nums1[curr_pt] = nums1[last_n1]
                last_n1 -= 1
            else:
                nums1[curr_pt] = nums2[last_n2]
                last_n2 -= 1

            curr_pt -= 1