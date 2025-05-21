
users={("jhon","1234"):"admin",
       ("alice","abcd"):"editor"}

username=input("enter username")
password=input("enter passowrd")
creds=(username,password)
ids=users.keys()
if creds in ids:
    print(f"welcone,{users[creds]}")
else:
    print("invalid login")

