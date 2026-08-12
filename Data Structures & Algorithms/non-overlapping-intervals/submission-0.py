class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        # Sort by ending time
        for i in range(n):
            for j in range(i + 1, n):
                if intervals[i][1] > intervals[j][1]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]

        count = 0
        end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]

        return count