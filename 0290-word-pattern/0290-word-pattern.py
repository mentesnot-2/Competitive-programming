class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split(" ")
        if len(pattern)!=len(word): return False
        charToWord={}
        wordToChar={}
        for i,j in zip(pattern,word):
            if i in charToWord and charToWord[i]!=j:
                return False
            if j in wordToChar and wordToChar[j]!=i:
                return False
            charToWord[i]=j
            wordToChar[j]=i
            
        return True