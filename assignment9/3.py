f=True
lis=[]
while f:
    user = int(input("enter number"))
    if user%2==0:
        lis.append(user)
    else:
        print("odd number enterd")
        break
else: 
    print(lis)
print(lis)