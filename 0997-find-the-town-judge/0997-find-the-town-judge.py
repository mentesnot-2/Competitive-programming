class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0 for _ in range(n)]
        outgoing = [0 for _ in range(n)]

        for p1,p2 in trust:
            incoming[p2 - 1] += 1
            outgoing[p1 - 1] += 1


        for p in range(n):
            if incoming[p] == n -1 and outgoing[p] == 0:
                return p + 1
        return -1