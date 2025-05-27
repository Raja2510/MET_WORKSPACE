dic={"name":"alice",
     "city":"new york",
     "hobby":"coding"}
for i  in dic:
    if len(dic[i])<6:
        print(f"{i} : {dic[i].lower()}")
    else:
        print(f"{i} : {dic[i].upper()}")


