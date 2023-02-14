class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        num=sorted(intervals,key=lambda x:x[0])
        res=[num[0]]
        for i in range(1,len(intervals)):
            if res[-1][1]>=num[i][0]:
                res[-1][1]=max(res[-1][1],num[i][1])
            else:
                res.append(num[i])
        return res