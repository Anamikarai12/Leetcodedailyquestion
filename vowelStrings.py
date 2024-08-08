class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        c=0
        z=["a","e","i","o","u"]
        for i in range(left,right+1):
            a=words[i]
            if a[0] in z and a[-1] in z:
                c+=1
        return c
        
sol=Solution()
arr=["annu","aman","aab","ar"]
left=0
right=3
z=sol.vowelStrings(arr,left,right)
print(z)