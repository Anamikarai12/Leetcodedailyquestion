from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in asteroids:
            if mass>=i:
                mass+=i
            else:
                return False
        return True
a=[3,9,19,5,21]
mass=10

sol=Solution()
z=sol.asteroidsDestroyed(mass,a)
print(z)