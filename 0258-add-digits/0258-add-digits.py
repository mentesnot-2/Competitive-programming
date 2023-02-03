class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        else:
            tot = 0
            while (num != 0):
                tot = tot + (num % 10)
                num = num//10
            return self.addDigits(tot)
                