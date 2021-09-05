s="sstringbbbb"
d=[]
for i in s:
    if s.count(i)>1:
        if i not in d:
            d.append(i)
print(d)