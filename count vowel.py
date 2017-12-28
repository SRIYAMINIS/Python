count=0
name=input("enter the string")
for i in name:
    if i in ['A','E','I','O','U','a','e','i','o','u']:
        count=count+1
print("number of vowel in a string:",count)
