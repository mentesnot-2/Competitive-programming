class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(1,len(words)):
           words[i]=words[i-1] + words[i]
        return s in words
        