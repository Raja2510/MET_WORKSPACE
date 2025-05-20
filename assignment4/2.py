inventory={}

inventory.update({"apples":50,"oranges":40,"bananas":60})
inventory["apples"]=60
inventory.update({"grapes":25,"oranges":35})
a=inventory.pop("bananas")
print(a)
# print(inventory)
inventory.clear()
print(inventory)