class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        for i in nums:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        a.extend(b)
        return a
arr=[2,1,3,4]
sol=Solution()
z=sol.sortArrayByParity( arr)
print(z)

        