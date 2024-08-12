a=[1]
l_sum=[]
r_sum=[]
sum=0
for i in range(len(a)):
    l_sum.append(sum)
    sum+=a[i]

b=a[::-1]
sum=0
for i in range(len(b)):
    r_sum.append(sum)
    sum+=b[i]
r_sum=r_sum[::-1]
ans=[]
z=0
for i in range(len(a)):
    z=abs(l_sum[i]-r_sum[i])
    ans.append(z)
print(ans)