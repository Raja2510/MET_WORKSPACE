cart =[{"id":1, "name":"shirt","qty":1}]


product_id=int(input("enter product id : "))
product_name=input("enter product name : ")

user_cart={"pid":product_id,"pname":product_name}

if user_cart["pid"]==cart[0]["id"]:
    print("this item already exsists")
    print(f"cart {cart}")
else :
    cart.append({"id":product_id,"product name ": product_name})
    print(f"new cart {cart}")