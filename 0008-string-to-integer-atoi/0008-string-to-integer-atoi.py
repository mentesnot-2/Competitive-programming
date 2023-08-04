class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: Remove leading whitespace
        s = s.lstrip()

        # Step 2: Check for sign
        sign = 1
        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # Step 3: Read digits until non-digit or end of input
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break

        # Step 4: Apply sign and check for range
        num *= sign
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX

        return num
