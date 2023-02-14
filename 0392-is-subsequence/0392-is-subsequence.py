class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub = ""
        for i in range(len(t)):
            if t[i] in s and t[i] == s[len(sub)]:
                sub += t[i]
        
        return sub == s