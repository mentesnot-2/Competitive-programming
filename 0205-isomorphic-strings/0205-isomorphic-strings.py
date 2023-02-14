class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # word=s.split(" ")
        if len(s)!=len(t): return False
        charToWord={}
        wordToChar={}
        for i,j in zip(s,t):
            if i in charToWord and charToWord[i]!=j:
                return False
            if j in wordToChar and wordToChar[j]!=i:
                return False
            charToWord[i]=j
            wordToChar[j]=i
            
        return True