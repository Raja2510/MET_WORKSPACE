#::::::::::::::::::functions :::::::::::::::::: 
# def thing():
#     print("hello")

# thing()
# print("one")
# thing()

# def say_goodmorning():
#     print("good morning")


# def say_hello():
#     print("hello")
#     say_goodmorning()
# say_hello()
# say_goodmorning()

# def one_to_three():
#     print(1)
#     print(2)
#     print(3)
# def three_to_seven(is_vertical):
#     if is_vertical:
#         print(3)
#         print(4)
#         print(5)
#         print(6)
#         print(7)
#     else:
#         print(3,4,5,6,7)
# def seven_to_ten():
#     print(7)
#     print(8)
#     print(9)
#     print(10)

# three_to_seven(False)
# one_to_three()
# seven_to_ten()



# def greet(lang,name):

#     if lang == "en":

#         print(f"Hello {name}")

#     elif lang == "fr":

#         print(f"Bonjour {name}")

#     else:

#         print(f"Hola {name}")

# greet("fr","raja")
 
# def greet(lang):
#     output=""
#     if lang == "en":
#         output= "hello"

#     elif lang == "fr":

#         output= "bonjour"

#     else:
#         output="hola"
#     return output

# print(greet("fr"))
  
data=[{
    "name":"raja",
    "age":21
},      
{    "name":"teja",
    "age":20
    }
] 
def extract_names(detailes):
    name1=detailes[0]["name"]
    name2=detailes[1]["name"]
    return [name1,name2]
names= extract_names(data)
print(names)
def extract_ages(detailes):
    name1=detailes[0]["age"]
    name2=detailes[1]["age"]
    return [name1,name2]
ages= extract_ages(data)
print(ages)

