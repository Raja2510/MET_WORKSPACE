dic={"apple":2,
     "banana":3,
     "apricot":4,
     "berry":5}
sum=1
for i in dic:
    if i[0]=='a':
        sum*=dic[i]
print(sum)