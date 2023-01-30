class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set(nums3)
        lst=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                lst.append(i) 
        for j in nums2:
            if j in nums3 and j not in nums1:
                lst.append(j)
        return lst 