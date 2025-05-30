# def show_greeting(firstword, message):
#     print(firstword+" "+message)
# show_greeting("Hi","are you good")


# def show_greeting(*Words):# * helps use take in multiple attribute 
#     # print(Words)
#     for i in Words:
#         print(f"hi {i}")
# show_greeting("raja","teja")

#positional areguments should be always at the end (a=1 , b =2  , 3)-> worng (1 , a=2 , b=3)-> correct

# def show_greeting(**Words):# the postional arguments are converted into dictinory , doesnt accept key word argumrnts
#     print(Words)
#     # for i in Words:  
#     #     print(f"hi {i}")
# show_greeting(a="raja",b="teja")




def hel(word):
    
    final_sentance="hello "+word
    
    return final_sentance
a=hel("raja")
print(a)