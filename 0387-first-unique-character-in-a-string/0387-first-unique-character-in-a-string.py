class Solution:
    def firstUniqChar(self, s: str) -> int:
        val = Counter(s)
        ans = ''
    
        for i in val:
            if val[i] == 1:
                ans = i
                break
      
        return s.index(ans) if ans != '' else -1