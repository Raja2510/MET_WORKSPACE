#password_strength_checker

#generate password using methods and expressions
#check strength uisng  conditions
#store password rules in dictinory
#

#---categorites    criteria
#weak password      -1 
#fair password      -6
#good password      -8
#strong password    -12
#very_strong        -16

#mandates
#lowercase a-z
#uppercase A-B
#digits 0123456789
#special !@#$%^&*()

#---eleminate common pharases
    #sequencees - 123 -abc -345
    #common -password admin user login welcome



weak       =0
fair       =6
good       =8
strong     =12
very_strong        =16

password= input("Enter the password : ")

password_length =len(password)
print(password_length)


mandatory_rules={
    "lowercase":"abcdefghijklmnopqrstuvwxys",
    "uppercase":"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits" : "0123456789",
    "special":"!@#$%^&*()_+-={}[]:"
}

if password_length>very_strong:
    password_strength ="very strong password"
elif password_length>strong:
    password_strength ="strong password"
elif password_length>good:
    password_strength ="good password"
elif password_length>fair:
    password_strength ="fair password"
elif password_length>weak:
    password_strength ="weak password"
else:
    print("password cannot be blank")

is_invalid=password.isalnum()#returns true if the string is alphanumric

if is_invalid:
    print("password is invalid")
else:
    print(f"password {password_strength } and valid")