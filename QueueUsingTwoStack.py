n=int(input())
queue=[]
ans=[]
while n>0:
    a=list(map(int,input().split()))
    if a[0]==1:
        queue.append(a[1])
    elif a[0]==2:
        queue.pop(0)
    elif a[0]==3:
        ans.append(queue[0])
    n-=1
for i in ans:
    print(i)
    