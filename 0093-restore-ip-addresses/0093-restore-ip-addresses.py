class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        res = []
        def backtrack(i,dots,curIp):
            if dots == 4 and i == len(s):
                res.append(curIp[:-1])
                return
            if dots > 4:
                return
            for j in range(i,min(i + 3,len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1,dots + 1,curIp + s[i:j + 1] + ".")
            return res
        return backtrack(0,0,"")
                    
        