from collections import Counter
class Solution:
    def findLucky(self, arr) :
        count=Counter(arr)
        c=[]
        for i,j in count.items():
            if i == j:
                c.append(i)
            else:
                continue
        if len(c)>0:
            return max(c)
        return -1
a=[2,2,3,4]
sol=Solution()
b=sol.findLucky(a)
print(b)