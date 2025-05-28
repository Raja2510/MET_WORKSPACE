names=[]
for i in range(5):
    inp=input("enter name : ")
    names.append(inp)
key=input("enter the name you want to find ")
for x in names:
    if x== key:
        print(f"{key} is found")
        break
else:
    print(f"{key}is not found")