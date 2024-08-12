class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # a=[]
        # n=arr[:]
        # d={}
        # k=1
        # arr.sort()
        # for i in arr:
        #     if i not in d: 
        #         d[i]=k
        #         k+=1
            
            
        # for k in n:
        #     a.append(d[k])
        # return a

       
        a=[]
        n=arr[:]
        arr.sort()
        d={}
        j=0
        k=1
        for i in range(1,len(arr)+1):
            if arr[j] not in d: 
                d[arr[j]]=k
                k+=1
            
            j+=1
        for k in n:
            a.append(d[k])
        return a

sol=Solution()
a=[40,10,20,30]
z=sol.arrayRankTransform(a)
print(z)


                