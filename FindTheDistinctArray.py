class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(1,len(nums)+1):
            a.append(len(set(nums[:i]))-len(set(nums[i:])))
        return a
            
a=[1,2,3,4,5]
sol=Solution()
b=sol.minEnd(a)
print(b)