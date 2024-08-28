class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=[]
        c=0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
               c+=1
        a.append(c)
        c=0
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                c+=1
        a.append(c)
                
        return a
                
            
a=[4,1,3]
a1=[5,7]
sol=Solution()
b=sol.findIntersectionValues(a,a1)
print(b)