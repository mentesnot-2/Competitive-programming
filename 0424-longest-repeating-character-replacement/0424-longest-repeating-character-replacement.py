class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        
        l = 0
        rplc = {}
        
        for r in range(len(s)):
            rplc[s[r]] = 1 + rplc.get(s[r],0)
            
            if (r - l + 1) - max(rplc.values()) > k:
                rplc[s[l]]-=1
                l+=1
            ans = max(ans,r - l + 1)
        return ans
        
            
            
        