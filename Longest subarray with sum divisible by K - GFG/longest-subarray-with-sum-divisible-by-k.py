#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) :
	    mod_arr=[0 for i in range(n)]
	    maxLen=0
	    curSum=0
	    freq={}
	    for i in range(n):
	        curSum+=arr[i]
	        mod_arr[i]=((curSum%K)+K)%K
	        if mod_arr[i]==0:
	            maxLen=i+1
	        elif mod_arr[i] not in freq:
	            freq[mod_arr[i]]=i
	        else:
	            if (maxLen<(i-freq[mod_arr[i]])):
	                maxLen=i-freq[mod_arr[i]]
	    return maxLen
	    
	    
	    
	    
	    
	    
	   # maxLen=0
	   # for i in range(n):
	   #     sum1=0
	   #     for j in range(i,n):
	   #         sum1+=arr[j]
	   #         if sum1%K==0:
	   #              maxLen=max(maxLen,j-i+1)
	   # return maxLen
		#Complete the function



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends