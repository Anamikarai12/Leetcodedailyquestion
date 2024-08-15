class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i]-nums[j])==k and i<j:
                    c+=1
        return c


a=[1,2,3,4,5]
k=1
sol=Solution()
b=sol.countKDifference(a,k)
print(b)