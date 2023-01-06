class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        l=0
        substrng={}
        for r in range(len(s)):
            rep=substrng.get(s[r])
            if rep is not None and rep>=l:
                length=r-l
                l=1+rep
                res=max(res,length)
            substrng[s[r]]=r
        long=max(len(s)-l,res)
        return long