class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints[:k])
        score=sum(cardPoints[:k])
        for i in range(1,k+1):
            score=score-cardPoints[k-i]+cardPoints[-i]
            total=max(score,total)
        return total