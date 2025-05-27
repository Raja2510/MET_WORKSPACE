#defenitive loop - for loop

#for loop

# fruits =["apple","banana","cherry","dragonfruit"]

# for item in fruits:
#     print(item)
#     if item == "cherry":
#         break


# name = "charminar"
# count=0
# for item in name:
#     # print(item)
#     if item in ["a","e","i","o","u"] :
#         count+=1
# print(f"we have {count} vowels")


# for loop terminates 1.when the iteration of the sequence ends 2. when it encounters break statements

# name = "beautiful"
# count=0
# for item in name:
#     if item in ["a","e","i","o","u"] :
#         continue#stops the cuttent iteration and continues the next itrration 
#     print(item)



#for loop in tuple /same
# fruits =("apple","banana","cherry","dragonfruit")
# for item in fruits:
#     print(item)
 
#for loop in set sqeuential but its random
# fruits ={"apple","banana","cherry","dragonfruit"}
# for item in fruits:
#     print(item)
 

# info={
#     "name":"raja",
#     "age":"25"
# }
#gives keys by default
# for item in info:
#     print(item)
# for item in info.values():
#     print(item)

# person={
#     "name":"joy",
#     "age":45,
#     "hobbies":["dancing","swimming","reading"]

 
# }
# #printing hobbies
# for item in person:
#     if item == "hobbies":
#         for i in person[item]:
#             print(i)


# numbers = [1,4,7,10,13,16]

# sum=0
# for i in numbers:
#     if i%2 ==0:
#         sum+=i
# print(sum)