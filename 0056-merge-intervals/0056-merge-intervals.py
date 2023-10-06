class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        final = [intervals[0]]
        for i in range(1,len(intervals)):
            if final[ - 1][1] >= intervals[i][0]:
                final[-1][1] = max(final[-1][1],intervals[i][1])
            else:
                final.append(intervals[i])
        return final
        