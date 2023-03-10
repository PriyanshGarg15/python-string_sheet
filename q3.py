def reverse(string):
    if len(string) == 0:
        return 
    else:
        return string[::-1]
a = str(input("Enter the string to be reversed: "))
print(reverse(a))
