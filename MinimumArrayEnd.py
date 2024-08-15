class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        a=[x]
     
        i=x+1
        while len(a)<n:
            if i & x == x:
                a.append(i)
                
            i+=1
                
        print(a)
        return a[-1]
a=3
b=4
sol=Solution()
b=sol.minEnd(a,b)
print(b)