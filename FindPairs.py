class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # if not (1 <= len(nums) <= 10**4) or not all(-10**7 <= x <= 10**7 for x in nums) or  not (0 <= k <= 10**7):
        #     return 0
        # c=set()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if abs(nums[i]-nums[j])==k and i!=j:
        #             if (nums[i],nums[j]) not in c and (nums[j],nums[i]) not in c:
        #                 c.add((nums[i],nums[j]))
        # return len(c)

        s=set()
        d=set()
        for num in nums:
            if num-k in s:
                d.add((num-k,num))
            if num+k in s:
                d.add((num,num+k))
            s.add(num)
        return len(d)
                    
a=[1,2,3,4,5]
k=1
sol=Solution()
b=sol.findPairs(a,k)
print(b)