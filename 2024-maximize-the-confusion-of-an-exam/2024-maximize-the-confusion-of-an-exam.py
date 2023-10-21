class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_length = 0
        max_count = 0
        left = 0

        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                max_count += 1

            while max_count > k:
                if answerKey[left] == 'T':
                    max_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        max_count = 0
        left = 0

        for right in range(len(answerKey)):
            if answerKey[right] == 'F':
                max_count += 1

            while max_count > k:
                if answerKey[left] == 'F':
                    max_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
