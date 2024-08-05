from collections import Counter
words1=["leetcode","is","amazing","as","is"]
words2=["amazing","leetcode","is"]
w1=Counter(words1)
w2=Counter(words2)
c=0
for i,j in w1.items():
    if i in w2 and w2[i]==1 and j==1:
        c+=1
print(c)