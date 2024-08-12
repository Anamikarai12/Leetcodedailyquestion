class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        
        TotalTime=arrivalTime+delayedTime
        return TotalTime%24
        
sol=Solution()
a=1
b=25
z=sol.findDelayedArrivalTime(a,b)
print(z)