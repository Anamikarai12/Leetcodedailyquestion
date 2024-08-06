class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        a=1
        for i in range(1,len(nums)):
            if nums[i]>=nums[i-1] :
                a+=1
                if a==len(nums):
                    return True
        b=1
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                b+=1
                if b==len(nums):
                    return True
        return False
solution=Solution()
nums=[1,2,5,3]
z=solution.isMonotonic(nums)
print(z)
                
        

        