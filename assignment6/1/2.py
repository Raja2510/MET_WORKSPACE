categorie={
    "cloths":["shirt","jeans"],
    "electronics":["phone","charger"]
}

userin=input("enter category name: ")

if userin in categorie:
    print(categorie[userin])
else:
    print("invalid category")