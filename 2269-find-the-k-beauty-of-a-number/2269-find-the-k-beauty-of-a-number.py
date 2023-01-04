class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        count=0
        if k == 1: return len([i for i in s if i != "0" and num % int(i) == 0])
        for i in range(len(s)-k+1):
                if  int(s[i:i+k])!=0:
                    if int(s)% int(s[i:i+k])==0:
                        count+=1
        return count