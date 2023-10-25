class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dct = {}
        ans = 0
        for i in time:
            rem = i % 60
            if rem == 0 and 0 in dct:
                ans+=dct[0]
            elif 60 - rem in dct:
                ans+=dct[60 - rem]
            if rem not in dct:
                dct[rem] = 0
            dct[rem]+=1
        return ans