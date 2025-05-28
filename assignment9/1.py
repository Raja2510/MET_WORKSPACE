listt=list(input("enter list"))
key =int(input("enter key "))
for i in listt:
    if int(i)== key:
        print(f"{key } is found")
        break
else:
    print(f"{key } is not found")
