s1=input()
s2=input()
for i in s1:
    for j in s2:
        if(i==j):
            s2=s2.replace(i,"")
print(s2)
