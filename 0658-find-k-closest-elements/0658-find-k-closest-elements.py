class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda k: abs(k - x))
        val = sorted(arr[:k])
        return val
        