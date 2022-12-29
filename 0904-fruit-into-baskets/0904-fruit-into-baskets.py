class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        length = len(fruits)
        left, current = 0, {}
        currentLength, longestLength = 0, 0
        
        for right in range(0, length):
            current[fruits[right]] = current.get(fruits[right], 0) + 1
            
            while len(current) > 2:
                current[fruits[left]] -= 1
                if current[fruits[left]] == 0:
                    del current[fruits[left]]
                left += 1   
                
            currentLength  = right - left + 1
            longestLength = max(longestLength, currentLength)     
            
        return longestLength
        