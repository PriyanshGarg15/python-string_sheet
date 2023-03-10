s1=input()
l= []
for character in s1:
      if s1.count(character) > 1:
         if character not in l:
            n=s1.count(character)
            l.append(character)
            l.append(n)
if(len(l)!=0):
    print("these are the duplicates:-")
    for i in range(0,len(l),2):
        for i in range(0,len(l),2):
          print(l[i],"comes",l[i+1],"times")
else:
    print("no duplicates")
