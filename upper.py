a=input("enter the string")
count1=0
count2=0
for i in a:
    if(i.isupper()):
        count1=count1+1
        
    if(i.islower()):
        count2=count2+1 
print("count the upper case letters:",count1)          
print("\ncount the upper case letters:",count2) 
