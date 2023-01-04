class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        l=len(s)
        count=0
        for i in range(l):
            if i+k<=l:
                window=int(s[i:i+k])
                if window!=0 and int(s)%window==0:
                    count+=1
        return count