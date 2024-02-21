
# firstList = [[0,2],[5,10],[13,23],[24,25]]
# secondList = [[1,5],[8,12],[15,24],[25,26]]

# res = [[1,2],[5,5], [8,10], [12,13], [15,23], [24,24], [25,25]]
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        i = j = 0
        res = []

        while i < len(firstList) and j < len(secondList):
            i_start, i_end = firstList[i]
            j_start, j_end = secondList[j]

            # check if intersection exists
            if i_start > j_end:
                j += 1
            elif j_start > i_end:
                i += 1
            else:
                res.append([max(i_start, j_start), min(i_end, j_end)])

                if i_end > j_end:
                    j += 1
                else:
                    i += 1

        return res


        