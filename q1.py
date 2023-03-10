s1=input()
l= []
for character in s1:
    if character not in l:
        n=s1.count(character)
        l.append(character)
        l.append(n)
    
for i in range(0,len(l),2):
    print(l[i],"comes",l[i+1],"times")
