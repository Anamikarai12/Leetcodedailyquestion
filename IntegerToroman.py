#integer to roman
a=8
l=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
res=""
for i,j in l:
    while a>=i:
        res+=j
        a-=i
print(res)