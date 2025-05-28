fruits={
    "apple":10,
    "banana":20,
    "cherry":30

}

fruits.update({"dragon":30})
print(fruits)
fruits.update({"apple":50})
print(fruits)
del fruits["banana"]
print(fruits)