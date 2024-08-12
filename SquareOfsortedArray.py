class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in nums:
            a.append(i*i)
        a.sort()
        return a

sol=Solution()
a=[-4,-1,0,3,10]
z=sol.sortedSquares(a)
print(z)