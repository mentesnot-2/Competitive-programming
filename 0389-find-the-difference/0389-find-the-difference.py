class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=Counter(s)
        t=Counter(t)
        res=""
        for i in t:
            if i not in s:
                while t[i]:
                    res+=i
                    t[i]-=1
            elif t[i]>s[i]:
                m=t[i]-s[i]
                while m:
                    res+=i
                    m-=1
        return res