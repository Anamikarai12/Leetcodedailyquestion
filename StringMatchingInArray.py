class Solution:
    def stringMatching(self, words):
        c=[]
        for i in words[:]:
            for j in words[:]:
                if j in i and j!=i:
                    c.append(j)
                    words.remove(j)
        return c
a=["mass","as","hero","superhero"]
sol=Solution()
b=sol.stringMatching(a)
print(b)