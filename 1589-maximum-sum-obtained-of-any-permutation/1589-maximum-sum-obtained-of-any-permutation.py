class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        arr = [0] * n

        for start, end in requests:
            arr[start] += 1
            if end + 1 < n:
                arr[end + 1] -= 1

        for i in range(1, n):
            arr[i] += arr[i - 1]

        arr.sort(reverse=True)
        nums.sort(reverse=True)

        mod = 10**9 + 7
        result = sum(arr[i] * nums[i] for i in range(n)) % mod

        return result
