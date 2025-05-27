tup=("sam","jhon","alex", "bob")

for i in tup:
    if len(i) <4:
        print(i.upper())
    else:
        print(i.capitalize())