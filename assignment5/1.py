temp=int(input("enter temprature "))
metric=input("specift Celsius/faherheit ")
new_temp=temp
if metric.lower() == "fahrenheit":
    temp=5/9*(new_temp-32)
elif metric.lower() == "celsius":
    temp=((9/5*temp)+32)

print(f"new temp = {temp}")