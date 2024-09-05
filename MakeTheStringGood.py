class Solution:
    def makeGood(self, s: str) -> str:
        a=[]
        for i in s:
            if a and abs(ord(i)-ord(a[-1]))==32:
                a.pop()
            else:
                a.append(i)
        return "".join(a)
a1="leEeetcode"
sol=Solution()
b=sol.makeGood(a1)
print(b)