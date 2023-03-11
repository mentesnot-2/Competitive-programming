#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        prefixSum=[0]
        for i in range(n):
            prefixSum.append(prefixSum[-1]+arr[i])
        freq={0:1}
        for j in range(1,len(prefixSum)):
            if (prefixSum[j]-s) in freq:
                # return prefixSum[j]-s
                return [freq[prefixSum[j]-s],j]
            freq[prefixSum[j]]=j+1
        return [-1]
            
       #Write your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends