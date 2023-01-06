class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict1={}
        dict2={}
        for i in words1:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        for j in words2:
            if j in dict2:
                dict2[j]+=1
            else:
                dict2[j]=1
        # return dict1,dict2
        count=0
        for k in dict1:
            if k in dict2:
                if dict1[k]==1 and dict2[k]==1:
                    count+=1
        return count
