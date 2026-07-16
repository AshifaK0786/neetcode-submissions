"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):

                start1 = intervals[i].start
                end1 = intervals[i].end

                start2 = intervals[j].start
                end2 = intervals[j].end

                
                if start1 < end2 and start2 < end1:
                    return False

        return True