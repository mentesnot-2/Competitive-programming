class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid = []
        
        for val in asteroids:
            while asteroid and val < 0 and asteroid[-1] > 0:
                if val + asteroid[-1] > 0 : val = 0
                elif val + asteroid[-1] < 0: asteroid.pop()
                else:
                    val = 0
                    asteroid.pop()
            if val != 0: asteroid.append(val)
                    
        return asteroid
        
        