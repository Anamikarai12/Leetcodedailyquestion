class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        nums1=[]
        nums2=[]
        for i in range(0,len(nums),2):
            nums1.append(nums[i])
            if i+1<len(nums):
                nums2.append(nums[i+1])
        if len(set(nums1)) != len(nums1) or len(set(nums2))!= len(nums2):
            return False
        if len(set(nums1))==len(set(nums2)):
            return True
        return False
sol=Solution()
a=[1,1,2,2,3,4]
z=sol.isPossibleToSplit(a)
print(z)