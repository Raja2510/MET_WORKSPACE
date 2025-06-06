payment_choice=int(input("1.phonepe\n2.paytm\n3.gpay\n"))
class phonepe:
    def __init__(self):
        pass
    def recive_payment(self):
        print("phonepe recived payment")
class paytm:
    def __init__(self):
        pass
    def recive_payment(self):
        print("paytm recived payment")
class gpay:
    def __init__(self):
        pass
    def recive_payment(self):
        print("gpayrecived payment")

def recive_payment(prov):
    prov.recive_payment()

if payment_choice==1:
    provider=phonepe()
if payment_choice==2:
    provider=paytm()
if payment_choice==3:
    provider=gpay()

recive_payment(provider)