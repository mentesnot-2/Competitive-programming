class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        for i in s:
            if i == "#":
                if stackS: 
                    stackS.pop()
            else:
                stackS.append(i)
        stackT = []
        for i in t:
            if i == "#":
                if stackT: 
                    stackT.pop()
            else:
                stackT.append(i)
        return stackS == stackT