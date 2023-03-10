s1=input("enter string=")
s1=s1.split()
count=0
for i in s1:
    if(i=="the"):
        count=count+1
print("the is",count,"times in string")
