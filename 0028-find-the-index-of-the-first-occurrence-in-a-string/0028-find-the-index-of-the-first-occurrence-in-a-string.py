class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack) or (len(needle)==len(haystack) and needle!=haystack):
            return -1
        if len(haystack)==1 and (needle==haystack):
            return 0
        l=0
        r=len(needle)-1
        while l<=r and r<len(haystack)+1:
            if haystack[l:r+1]==needle:
                return l
            l+=1
            r+=1
        return -1
        
        