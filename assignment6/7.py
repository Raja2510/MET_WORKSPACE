students={
    "alice":(85,90,78),
    "bob":( 50,45,60)

}

userinput=input("enter student name: ")
if userinput in students:
    avg=(students[userinput][0]+students[userinput][1]+students[userinput][2])/3
    print(f"average ={avg}")   
    if avg >= 60:
        print("pass")
    else:
        print("fail")
else:
    print("student not found")
        