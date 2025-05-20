book={

}
book.update({"title":"python 101",
             "author":"mike",
             "year":2021}
)
book["year"]=2022
a=book.get("publisher","unknown_punlisher")
print(a)

k=book.keys()
v=book.values()
print(k)
print(v)
book.clear()
print(book)