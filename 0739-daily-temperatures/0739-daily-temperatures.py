class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for indx,value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                stackVal,stackIndx = stack.pop()
                res[stackIndx] = (indx - stackIndx)
            stack.append((value,indx))
        return res