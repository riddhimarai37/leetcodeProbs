class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        # sort intervals by start values 
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        left = 0
        right = 1

        while right <= len(intervals):
            # merge the intervals
            while right < len(intervals) and intervals[left][1] >= intervals[right][0]:
                start1 = intervals[left][0]
                start2 = intervals[right][0]
                end1 = intervals[left][1]
                end2 = intervals[right][1]

                intervals[left] = [min(start1, start2), max(end1, end2)]
                right += 1
            # update with merged interval
            res.append(intervals[left])
            left = right
            right += 1

        return res






















        # intervals.sort(key=lambda x: x[0])
        # merged = [intervals[0]]

        # for interval in intervals:
        #     if merged[-1][1] < interval[0]:
        #         merged.append(interval)
        #     else:
        #         merged[-1][1] = max(merged[-1][1], interval[1])
            
        # return merged



