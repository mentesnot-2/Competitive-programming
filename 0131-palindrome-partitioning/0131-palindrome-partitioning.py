class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def palindrome(s):
            n = len(s)
            i, j = 0, n - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def partition1(res,indx,s,cur):
            if (indx) == len(s):
                res.append(cur.copy())
                return
            t = ""
            for i in range(indx,len(s)):
                t+=s[i]
                if palindrome(t):
                    cur.append(t)
                    partition1(res,i + 1,s,cur)
                    cur.pop()
            return res
        return (partition1([],0,s,[]))
        