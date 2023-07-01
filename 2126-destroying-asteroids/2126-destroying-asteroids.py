class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        
        for val in asteroids:
            if val > mass: return False
            mass+=val
        return True