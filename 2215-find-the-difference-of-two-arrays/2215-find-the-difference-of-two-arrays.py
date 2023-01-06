class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output=[]
        output1=[]
        output2=[]
        c1=Counter(nums1)
        c2=Counter(nums2)
        for i in c1:
            if i not in c2:
                output1.append(i)
        for i in c2:
            if i not in c1:
                output2.append(i)
        output.append(output1)
        output.append(output2)
        return output
        