def add(a,b):
    print(a+b)
def subract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
a = int(input("enter the first : "))
b = int(input("enter the secoend : "))
operator=input("enter operator : ")
if operator == "+":
    add(a,b)
elif operator=="-":
    subract(a,b)
elif operator=="*":
    multiply(a,b)
elif operator=="/":
    divide(a,b)


