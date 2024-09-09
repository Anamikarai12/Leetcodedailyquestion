class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m=[]
        n=[]
        for i in s:
            if i=="#":
                if m:
                    m.pop()
            else:
                m.append(i)
        for i in t:
            if i=="#":
                if n:
                    n.pop()
            else:
                n.append(i)
        if m==n:
            return True
        return False
                    
a="ab#ca"
b="ab#ca"

sol=Solution()
z=sol.backspaceCompare(a,b)
print(z)