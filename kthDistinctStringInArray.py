def kthDistinct( arr, k):
        a=[]
        for i in range(len(arr)):
            if arr[i]  not in arr[:i] and arr[i] not in arr[i+1:]:
                a.append(arr[i])
        if len(a)>=k:
            return a[k-1]
        else:
            return ""

        
       
arr=["d","b","c","b","c","a"]
k=2
z=kthDistinct( arr, k)
print(z)

        