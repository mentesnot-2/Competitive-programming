class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        val=candies[0]
        for i in range(1,len(candies)):
            if candies[i]>val:
                val=candies[i]
        lst=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=val:
                lst.append(True)
            else:
                lst.append(False)
        return lst
        