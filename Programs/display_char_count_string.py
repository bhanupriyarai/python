s="stringfdss"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key, value in d.items():
        print(key, ":", value, end=",")

