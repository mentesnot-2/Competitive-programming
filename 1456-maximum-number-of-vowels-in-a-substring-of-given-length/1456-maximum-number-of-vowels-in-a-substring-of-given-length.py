class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel=['a', 'e', 'i', 'o','u']
        count=0
        res=0
        l=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
        res=max(res,count)
        for j in range(k,len(s)):
            if s[l] in vowel:
                count-=1
            if s[j] in vowel:
                count+=1
            l+=1
            res=max(res,count)
        return res
                