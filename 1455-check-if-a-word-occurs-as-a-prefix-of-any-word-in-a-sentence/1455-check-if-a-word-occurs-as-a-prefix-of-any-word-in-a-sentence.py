class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s=sentence.split(" ")
        count=0
        for i,j in enumerate(s):
            if j.startswith(searchWord):
                return i+1
        return -1