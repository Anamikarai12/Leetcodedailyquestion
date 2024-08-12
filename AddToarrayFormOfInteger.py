class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        sum=0
        for i in num:
            sum=(sum*10)+i
        b=sum+k
        c=[]
        while b>0:
            digit=b%10
            c.append(digit)
            b=b//10
        return c[::-1]

sol=Solution()
a=[1,2,0,0]
k=34
z=sol.addToArrayForm(a,k)
print(z)