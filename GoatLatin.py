class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=["a","e","i","o","u","A","E","I","O","U"]
        a=list(sentence.split())
        k=1
        b=[]
        for i in a:
            z=""
            if i[0] in s:
                z+=i
            else:
                z+=i[1:]
                z+=i[0]
                
            z+="ma"
            z+="a"*k
            k+=1
            b.append(z)
        return f'{" ".join(b)}'
a1="apple"
sol=Solution()
b=sol.toGoatLatin(a1)
print(b)