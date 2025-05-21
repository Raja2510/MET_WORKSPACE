food={

    "idly":10,
    "dosa":20,
    "vada":15,
    "upma":100


}


item1=input("Enter item 1 :")
item1q=int(input("enter quantity of item 1 "))
item2=input("Enter item 2 :")
item2q=int(input("enter quantity of item 2 "))

item3=input("Enter item 3 :")
item3q=int(input("enter quantity of item 3 "))



total_price=(food[item1]*item1q)+(food[item2]*item2q)+(food[item3]*item3q)
print(total_price)