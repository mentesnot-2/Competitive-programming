class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for val in s:
            if not stack or val == "(" or val == "{" or val == "[":
                stack.append(val)
            else:
                if (val == "]" and stack[-1] == "[") or (val == ")" and stack[-1] == "(") or (val == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
        return True if stack == [] else False