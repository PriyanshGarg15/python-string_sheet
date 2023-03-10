s1=input()
length = len(s1)  
n =int(input("enter parts u want to break in="))
char = int(length/n)
if(length % n != 0):  
        print("Sorry this string cannot be divided into " + str(n) +" equal parts");  
else:  
    for i in range(0, length, char):  
        
        part = s1[ i : i+char]
        print(part,end=",")
