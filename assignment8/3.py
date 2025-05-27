string="Welcome to Python loops"
vowels={"a","e","i","o","u"}
count=0
for i in string:
    if i.lower() in vowels:
        count+=1
print(count)