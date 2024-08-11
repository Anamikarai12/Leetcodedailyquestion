class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        b=''
        for i in nums:
            b+=str(i)
        c=[]
        for i in b:
            c.append(int(i))
        return c
sol=Solution()
a=[13,25,88,77]
z=sol.separateDigits(a)
print(z)