tags={"python","fastapi","backend"}
newtag=input("enter new tag: ")
if newtag in tags:
    print("tag already exsist")
else:
    tags.add(newtag)

    print(f"updated list {tags}")