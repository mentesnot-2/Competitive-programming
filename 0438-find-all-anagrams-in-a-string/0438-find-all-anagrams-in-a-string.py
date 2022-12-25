class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        dicP,dicS={},{}
        for i in range(len(p)):
            dicP[p[i]]=1+dicP.get(p[i],0)
            dicS[s[i]]=1+dicS.get(s[i],0)
        res=[]
        if dicP==dicS:
            res.append(0)
        
        l=0
        for r in range(len(p),len(s)):
            dicS[s[r]]=1+dicS.get(s[r],0)
            dicS[s[l]]-=1
            if dicS[s[l]]==0:
                dicS.pop(s[l])
            l+=1
            if dicS==dicP:
                res.append(l)
        return res