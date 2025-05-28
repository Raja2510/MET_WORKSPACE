#varible scopes:
name = "raja" # global variable
def show_attribute( gender): #these variable are only in function body ie scope is limited only for the functoin
                    #function tries to find the varible in local scope if there is none  then it will search at global scope
    global name
    name = "jhon"

    if gender=="f":
        print(f"{name} she have eyes")
    else:
        print(f"{name} he has eyes")
show_attribute("m")
show_attribute("f")

print(name)
#1 in a function  a argument in a finction has local scope 
#a local variable scope is confined to function body
#3 a local variale cannot be accessed outside
#5 cant have loacl and global variable references together inside a function
### cannot have local -> global but 
# we can have global -> local###