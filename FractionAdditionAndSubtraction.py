from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        a=eval(expression)
        c=Fraction(a).limit_denominator()
        if c.denominator==1:
            return f"{c}/1"
        return f"{c}"
a="-1/2+1/2"
sol=Solution()
b=sol.fractionAddition(a)
print(b)