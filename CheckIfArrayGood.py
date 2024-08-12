class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=max(nums)
        if len(nums)!=a+1 or len(set(nums))+1!=len(nums):
            return False
        c=0
        for i in nums:
            if i==a:
                c+=1

        if c==2:
            return True
        return False
sol=Solution()
a=[1,2,5,5,4,3]
z=sol.isGood(a)
print(z)