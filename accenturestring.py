a="a2b2c2d1"
b=[]
c=""
for i in range(1,len(a),2):
    b.append(a[i-1]*int(a[i]))
for i in b:
    c+=i
print(c[5])