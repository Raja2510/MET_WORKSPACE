food={

    "idly":10,
    "dosa":20,
    "somosa":15,
    "paneer":100


}


item1=input("Enter item 1 :")
item1q=int(input("enter quantity of item 1 "))

item2=input("Enter item 2 :")
item2q=int(input("enter quantity of item 2 "))

item3=input("Enter item 3 :")
item3q=int(input("enter quantity of item 3 "))

item4=input("Enter item 4 :")
item4q=int(input("enter quantity of item 4 "))

total_price=(food[item1]*item1q)+(food[item2]*item2q)+(food[item3]*item3q)+(food[item4]*item4q)
print(total_price)