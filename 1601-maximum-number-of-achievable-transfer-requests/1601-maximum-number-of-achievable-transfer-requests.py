class Solution:
    def __init__(self):
        self.answer = 0

    def maxRequest(self, requests, indegree, n, index, count):
        if index == len(requests):
            # Check if all buildings have an in-degree of 0.
            if all(indegree[i] == 0 for i in range(n)):
                self.answer = max(self.answer, count)
            return

        # Consider this request, increment and decrement for the buildings involved.
        indegree[requests[index][0]] -= 1
        indegree[requests[index][1]] += 1

        # Move on to the next request and also increment the count of requests.
        self.maxRequest(requests, indegree, n, index + 1, count + 1)

        # Backtrack to the previous values to move back to the original state before the second recursion.
        indegree[requests[index][0]] += 1
        indegree[requests[index][1]] -= 1

        # Ignore this request and move on to the next request without incrementing the count.
        self.maxRequest(requests, indegree, n, index + 1, count)

    def maximumRequests(self, n, requests):
        indegree = [0] * n
        self.maxRequest(requests, indegree, n, 0, 0)
        return self.answer
