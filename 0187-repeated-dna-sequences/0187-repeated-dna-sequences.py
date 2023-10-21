class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        rptd = {}
        l,r = 0,10
        ans = []
        while r <= len(s):
            rptd[s[l:r]] = 1 + rptd.get(s[l:r],0)
            l+=1
            r+=1
       
        for k in rptd:
            if rptd[k] > 1:
                ans.append(k)
        return ans
        