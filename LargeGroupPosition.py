class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        b=[]
        i=0
        j=1
        while j<len(s):
            if s[i]==s[j]:
                j+=1
                if j==len(s) and len(s[i:j])>2:
                    b.append([i,j-1])
            else:
                if len(s[i:j])>2:
                    b.append([i,j-1])
                i=j
                j=i+1
        return b
s = "abbxxxxzzy"
sol=Solution()
z=sol.largeGroupPositions( s)
print(z)
