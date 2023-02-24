class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long={}
        start=0
        longest=0
        for i in range(len(s)):
            if s[i] in long and long[s[i]]>=start:
                start=long[s[i]]+1
            longest=max(longest,i-start+1)
            long[s[i]]=i

        return longest
