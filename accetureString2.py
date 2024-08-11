a="ABC"
b="AABCCD"
a=list(a)
c=list(a)
b=list(b)
for i in a:
    if i in b:
        c.remove(i)
        b.remove(i)
print(b)