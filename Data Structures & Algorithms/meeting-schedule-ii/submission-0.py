"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        max_count= 0
        count = 0
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        sp = 0
        ep = 0
        while ep < len(end) and sp < len(start):
            if start[sp] < end[ep]:
                count+=1
                max_count = max(max_count, count)
                sp+=1
            elif start[sp] > end[ep]:
                count-=1
                max_count = max(max_count, count)
                ep+=1
            else:
                sp+=1
                ep+=1
        return max_count




