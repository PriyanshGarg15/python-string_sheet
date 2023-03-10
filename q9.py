s1=input()
s1=s1.split()
l1= 0
for i in s1:
  l2=len(i)
  if l2>l1:
    l1=l2
for i in s1:
  l3= len(i)
  if l3==l1:
    print("largest word is=",i)
l4= len(s1[0])
for i in s1:
  l5= len(i)
  if l5<l4:
    l4=l5
for i in s1:
  l6= len(i)
  if l6==l4:
    print("smallest word is=",i)
