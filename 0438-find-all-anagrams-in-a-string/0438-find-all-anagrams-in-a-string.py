class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dictP=Counter(p)
        dictS={}
        l=0
        res=[]
        for r in range(len(s)):
            dictS[s[r]]=dictS.get(s[r],0)+1
            if (r-l+1)==len(p):
                if dictS==dictP:
                    res.append(l)
                dictS[s[l]]-=1
                if dictS[s[l]]==0:
                    dictS.pop(s[l])   
                l+=1
        return res