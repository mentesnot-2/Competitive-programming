class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring_map = {}
        start = 0
        for i in range(len(s)):
            position = substring_map.get(s[i])
            if position is not None and position >= start:
                length = i - start
                start = position + 1
                longest = max(length, longest)
            substring_map[s[i]] = i
        longest = max(len(s) - start, longest)
        return longest