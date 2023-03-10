s1=input()
vowel=consonant=digit=whitespace=0
for i in s1:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="y"):
        vowel=vowel+1
    elif((ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90)):
        consonant=consonant+1
    elif(i.isdigit()):
        digit=digit+1
    elif(i==' '):
        whitespace=whitespace+1
print("number of vowels=",vowel)
print("number of consonant=",consonant)
print("number of digit=",digit)
print("number of whitespace=",whitespace)
