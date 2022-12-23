class Solution:
    def compress(self, chars: List[str]) -> int:
        fstptr=0
        slwptr=0
        times=1
        while fstptr<len(chars):
            if fstptr+1<len(chars) and chars[fstptr]==chars[fstptr+1]:
                fstptr+=1
                times+=1
                
            else:
                chars[slwptr]=chars[fstptr]
                slwptr+=1
                if times!=1:
                    for i in str(times):
                        chars[slwptr]=i
                        slwptr+=1
                fstptr+=1
                times=1
        return slwptr
                