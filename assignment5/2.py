# login ysster

users={
    "username":"raja",
    "password":"raja"

}

get_user=input("enter username: ")
get_pass=input("enter password: ")

if get_user.lower() ==users.get("username"):
    if get_pass.lower() == users.get("password"):
        print("login sucessful")
    else:
        print("wrong password")
else:
    print("wrong username")

