order={
    "item1":{"name":"laptop","price":700},
    "item2":{"name":"mouse","price":20}
}

iky=input("enter itemkey: ")
listt=list(order.keys())

if iky == listt[0]:
    print(order[iky])
elif iky == listt[1]:
    print(order[iky])
else:
    print("invalid item")

