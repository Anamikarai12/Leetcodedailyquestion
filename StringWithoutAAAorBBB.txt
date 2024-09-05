class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res=""
        while a>0 or b>0:
            if a<b:
                if b>0:
                    res+="b"
                    b-=1
                if b>0:
                    res+="b"
                    b-=1
                if a>0:
                    res+="a"
                    a-=1
            elif b<a:
                if a>0:
                    res+="a"
                    a-=1
                if a>0:
                    res+="a"
                    a-=1
                if b>0:
                    res+="b"
                    b-=1
            else:
                if a>0:
                    res+="a"
                    a-=1
                if b>0:
                    res+="b"
                    b-=1
        return res

                
a=1
b=2
sol=Solution()
z=sol.strWithout3a3b(a,b)
print(z)