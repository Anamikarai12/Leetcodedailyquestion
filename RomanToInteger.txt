#roman to integer
a="VI"
l={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
res=0
for i in range(len(a)):
    if i+1<len(a) and l[a[i]]<l[a[i+1]]:
        res-=l[a[i]]
    else:
        res+=l[a[i]]
print(res)