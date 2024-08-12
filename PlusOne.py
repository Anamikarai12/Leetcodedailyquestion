class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # n=len(digits)
        # k=1
        # t=0
        # for i in range(n-1,-1,-1):
        #     t=digits[i]+k
        #     digits[i]=t%10
        #     k=t//10
        # if k:
        #     digits.insert(0,k)
        # return digits       
        sum=0
        for i in digits:
            sum=sum*10+i
        b=sum+1
        c=[]
        while b>0:
            digit=b%10
            c.append(digit)
            b=b//10
        return c[::-1]
sol=Solution()
a=[1,2,0,0]
z=sol.plusOne(a)
print(z)