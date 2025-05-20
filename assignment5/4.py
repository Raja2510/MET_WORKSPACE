bill=int(input("enter bill amount: "))

if bill>100:
    print(f"10% discout : bill amount {bill - bill*(10/100)}")
elif bill>50:
    print(f"5% discout : bill amount {bill - bill*(5/100)}")
else:
    print(f"no discout : bill amount {bill}")