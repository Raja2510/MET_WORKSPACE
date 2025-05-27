num=[10,25,36,40]
for i in num:
    a=i**(1/2)
    if a%1==0:
        print(f"{i} is a perfect square ")
        break
