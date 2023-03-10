s1=input("enter string=")
s2=input("enter substring=")
s1=s1.split()
count=0
for i in s1:
    if(i==s2):
        count=count+1
print("given substring is",count,"times in string")
