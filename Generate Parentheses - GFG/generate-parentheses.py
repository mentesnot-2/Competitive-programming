#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        stack = []
        res = []

        def backtrack(openN,closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            if openN < n:
                stack.append("(")
                backtrack(openN + 1,closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN + 1)
                stack.pop()
            return res
        return backtrack(0,0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends