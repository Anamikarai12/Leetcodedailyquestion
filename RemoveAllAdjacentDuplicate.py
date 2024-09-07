class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        i=1
        a.append(s[0])
        while i<len(s):
            if len(a)>0 and  s[i]==a[-1] :
                a.pop()
            else:
                a.append(s[i])
            i+=1
            
        return "".join(a)
a="abbaca"

sol=Solution()
z=sol.removeDuplicates(a)
print(z)