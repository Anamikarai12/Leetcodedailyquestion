class Solution:
    def subArrayRanges(self, nums) -> int:
        
        n=len(nums)
        sum=0
        for i in range(n):
            min_val=max_val=nums[i]
            for j in range(i,n):
                min_val=min(min_val,nums[j])
                max_val=max(max_val,nums[j])
                
                sum+=(max_val-min_val)
        return sum
a1=[1,2,3]
sol=Solution()
b=sol.subArrayRanges(a1)
print(b)