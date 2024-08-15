from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for i,n in count.items():
            if n%2==0:
                continue
            else:
                return False
        return True
        
a=[2,2,1,3,1,3]
sol=Solution()
b=sol.divideArray(a)
print(b)