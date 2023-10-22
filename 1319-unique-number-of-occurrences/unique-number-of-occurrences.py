class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        occur = {}

        for n in arr:
            if n not in occur:
                occur[n] = 1
            else:
                occur[n] += 1


        num_of_occur = set()

        for n in occur:
            num_of_occur.add(occur[n])

        if len(occur) != len(num_of_occur):
            return False

        return True
        