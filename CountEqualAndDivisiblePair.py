class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    c+=1
        return c


a=[3,1,2,2,2,1,3]
k=2
sol=Solution()
b=sol.countPairs(a,k)
print(b)