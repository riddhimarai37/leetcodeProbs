class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []

        for n in nums:
            if n > 0 or n == 0:
                pos.append(n)
            else:
                neg.append(n)

        neg = list(reversed(neg))

        for i in range(len(neg)):
            neg[i] = abs(neg[i])

        i = 0
        j = 0

        while i < len(neg) and j < len(pos):
            if neg[i] < pos[j]:
                ans.append(pow(neg[i],2))
                i+=1
            else:
                ans.append(pow(pos[j],2))
                j += 1

        while i < len(neg):
            ans.append(pow(neg[i],2))
            i += 1

        while j < len(pos):
            ans.append(pow(pos[j],2))
            j += 1

        return ans



