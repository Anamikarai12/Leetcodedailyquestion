class Solution:
    def minimizedStringLength(self, s: str) -> int:
        s=set(s)
        return len(s)
a="abbaca"

sol=Solution()
z=sol.minimizedStringLength(a)
print(z)