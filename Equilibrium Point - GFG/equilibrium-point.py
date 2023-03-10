# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if sum(A[1:])==0:
            return 1
        total=0
        for i in range(N):
            total+=A[i]
        res=0
        for i in range(N):
            res+=A[i]
            if total-res==res-A[i]:
                return i+1
        if sum(A[:N-1])==0:
            return N
        return -1
        # Your code here



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends