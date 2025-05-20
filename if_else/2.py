# Conditions if else

# total_bill=3000
# user_choice=input("enter payment mode")
# print("starting your checkout") 


# if user_choice.lower()=="phonepe": # using lower()ti convert input to lowercase
#     print("redirecting to phonepe")
#     print("opening pay panal...")

# #two way contitions
# if user_choice.lower()=="phonepe": 
#     print("redirecting to phonepe")
#     print("opening pay panal...")
# else:
#     print("redirecting to paytm")
#     print("opening pay panal...")

#combo 3 
# if user_choice.lower()=="phonepe": 
#     print("redirecting to phonepe")
# elif user_choice.lower()=="paytm":
#     print("opening pay panal...")
# elif user_choice.lower()=="gpay":
#     print("redirecting to gpay")

# combo#4
# if user_choice.lower()=="phonepe": 
#     print("redirecting to phonepe")
# elif user_choice.lower()=="paytm":
#     print("opening pay panal...")
# elif user_choice.lower()=="gpay":
#     print("redirecting to gpay")
# else:
#     print("payment mode not accepted")



##only these 4 combinitons can esisit together
# if #if else #if elif #if elif else    
#in any given combination only one block can execute
#there can be any number of elif chains.
# # 
# print(f"processing Rs.{total_bill}")



# x=2
# if x>6:
#     print("hello")
# elif x>1:
#     print("hello2")
# else:
#     print("hello3")



#-------nested-----------
# has_membership=True
# purchase_amount=120
# if has_membership:
#     print("Welcome, member")
#     if purchase_amount> 100:
#         print("you get 15% off")
#     else:
#         print("you get 10% off")
# else:
#     print("no discount")


#----------login system-------------
users= {
    "username":"raja1234",
    "password":"password"
}

username=input("Enter username: ")
password=input("Enter password: ")

correct_password=users.get("password")
correct_username=users.get("username")

# if username == correct_password :
#     if password == correct_password:
#         print("login successesful")
#     else:
#         print("invalid passowrd")
# else:
#     print("invalid username")

if username == correct_username and password == correct_password:
        print("login successesful")
   
else:
    print("invalid username")



