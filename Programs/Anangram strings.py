string1 = list(input("Inputstring:"))
string2 = list(input("String2:"))
v1 = sorted(string1)
v2 = sorted(string2)
if (len(string1) != len(string2)):
    print("Not anagram")
elif v1 == v2:
    print("it is anagram")
else:
    print("Not anagram")

