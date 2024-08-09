class Solution(object):
    def largestInteger(self, num):
        a=[]
        b=[]
        c=[]
        d=[]
        res=0
        for i in str(num):
            d.append(int(i))
        for i in d:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        a.sort(reverse=True)
        b.sort(reverse=True)
        a_index=0
        b_index=0
        for i in d:
            if i % 2 == 0:
                c.append(a[a_index])
                a_index += 1
            else:
                c.append(b[b_index])
                b_index += 1
        for i in range(len(c)):
            res=(res*10)+c[i]
        return res

arr=65875
sol=Solution()
z=sol.largestInteger( arr)
print(z)


        