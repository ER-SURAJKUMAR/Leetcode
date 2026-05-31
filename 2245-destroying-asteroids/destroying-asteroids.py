class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Sort the asteroids to always collide with the smallest one available
        asteroids.sort()
        
        for asteroid in asteroids:
            # If the planet is smaller than the asteroid, it gets destroyed
            if mass < asteroid:
                return False
            # Otherwise, absorb the asteroid's mass
            mass += asteroid
            
        return True