class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)*2
        a=[]
        for i in range(n):
            b=i%len(nums)
            a.append(nums[b])
        return a
        

sol=Solution()
arr=[1,2,1]
z=sol.getConcatenation(arr)
print(z)