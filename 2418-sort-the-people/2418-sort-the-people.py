class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if heights[i]>heights[j]:
                    temp1=names[j]
                    names[j]=names[i]
                    names[i]=temp1
                    temp=heights[j]
                    heights[j]=heights[i]
                    heights[i]=temp
        return reversed(names)
        