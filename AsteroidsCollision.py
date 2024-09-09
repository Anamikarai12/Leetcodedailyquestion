class Solution:
    def asteroidCollision(self, asteroids) :
        a=[]
        for i in asteroids:
            while a and  i<0 and a[-1]>0:
                if a[-1]<abs(i):
                    a.pop()
                    continue
                elif a[-1]==abs(i):
                    a.pop()
                break   
            else:
                a.append(i)
        return a

a=[5,10,-5]


sol=Solution()
z=sol.asteroidCollision(a)
print(z)