class Solution:
    def removeStars(self, s: str) -> str:
        a=[]
        for i in s:
            if i=="*":
                if a:
                    a.pop()
            else:
                a.append(i)
        return "".join(a)
        
a="abb**aca"

sol=Solution()
z=sol.removeStars(a)
print(z)