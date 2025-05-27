list=["python",'code',"loop","if","python","else","if"]

new_list=set(list)
for i in new_list:
    if i =="if" or i=="else":
        continue
    print(i)