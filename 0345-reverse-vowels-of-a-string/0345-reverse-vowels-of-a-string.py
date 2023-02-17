class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel={'a', 'e', 'i', 'o','u'}
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            if s[left].lower() in vowel and s[right].lower() in vowel:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif s[left].lower() in vowel and s[right].lower() not in vowel:
                right-=1
            elif s[right].lower() in vowel and s[left].lower() not in vowel:
                left+=1
            else:
                right-=1
                left +=1
        return "".join(s)