class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=0
        for i in range(1,len(nums)-1):
            if nums[i]==nums[i-1]:
                continue
            if nums[i-1]<nums[i]>nums[i+1] or nums[i-1]>nums[i]<nums[i+1]:
                n+=1
        return n
solution=Solution()
nums=[6,6,5,5,4,1]
z=solution.countHillValley(nums)
print(z)