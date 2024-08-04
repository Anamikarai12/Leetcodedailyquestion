#longest palindrome substring
a="ababbbbaab"
def lps(a):
    s=0
    e=0
    mx=0
    for i in range(len(a)):
        l=i
        r=i
        while l>=0 and r<len(a):
            if a[l]==a[r]:
                l-=1
                r+=1
            else:
                break
        length=r-l+1
        if length>mx:
            mx=length
            s=l+1
            e=r-1
        l=i
        r=i+1
        while l>=0 and r<len(a):
            if a[l]==a[r]:
                l-=1
                r+=1
            else:
                break
        length=r-l+1
        if length>mx:
            mx=length
            s=l+1
            e=r-1
    return a[s:e+1]
c=lps(a)
print(c)
