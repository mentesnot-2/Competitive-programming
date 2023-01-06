class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split(" ")
        s2=s2.split(" ")
        lst=[]
        for i in s1:
            if i not in s2 and s1.count(i)==1:
                lst.append(i)
        for j in s2:
            if j not in s1 and s2.count(j)==1:
                lst.append(j)
        return lst