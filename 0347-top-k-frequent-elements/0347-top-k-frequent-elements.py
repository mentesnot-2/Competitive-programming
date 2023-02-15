class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1=Counter(nums)
        c2=sorted(c1.items(), key=lambda x:x[1],reverse=True)
        lst=[]
        for i in c2:
            lst.append(i)
        close=[]
        for j in range(k):
            close.append(lst[j][0])
        return close