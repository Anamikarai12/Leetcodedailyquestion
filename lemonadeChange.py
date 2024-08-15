class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # five=0
        # ten=0
        # if bills[0]!=5:
        #     return False
        # for i in bills:
        #     if i==5:
        #         five+=1
        #     elif i==10:
        #         if five>0:
        #             five-=1
        #         else:
        #             return False
        #         ten+=1
        #     else:
        #         if five>0 and ten>0:
        #             five-=1
        #             ten-=1
        #         elif five>2:
        #             five-=3
        #         else:
        #             return False
        # return True
        

        b=[]

        for i in bills:
            if i==5:
                b.append(i)
            
            elif i==10:
                if 5 in b:
                    b.remove(5)
                    b.append(i)
                else:
                    return False
            else:
                if i==20:
                    if 10 in b and 5 in b:
                        b.remove(10)
                        b.remove(5)
                        b.append(i)
                    elif b.count(5)>2 :
                        b.remove(5)
                        b.remove(5)
                        b.remove(5)
                        b.append(20)
                    else:
                        return False
                    
            
                
        return True
a=[5,5,10,10,20]

sol=Solution()
b=sol.lemonadeChange(a)
print(b)
