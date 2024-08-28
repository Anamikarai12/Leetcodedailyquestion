class Solution(object):
    def minNumber(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        a=[]
        for i in nums1:
            if i in nums2:
                a.append(i)
            for j in nums2:
                if i==j: 
                    a.append(i)
                else:
                    if i<j:
                        a.append(i*10+j)
                    else:
                        a.append(j*10+i)

        a.sort()
        return a[0]
a=[4,1,3]
a1=[5,7]
sol=Solution()
b=sol.minNumber(a,a1)
print(b)