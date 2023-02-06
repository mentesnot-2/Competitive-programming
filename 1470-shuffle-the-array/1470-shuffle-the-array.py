class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num1=nums[:n]
        num2=nums[n:]
        shuffled=[]
        for i in range(len(num1)):
            shuffled.append(num1[i])
            shuffled.append(num2[i])
        return shuffled