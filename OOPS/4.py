#encapulation

class Person:
    def __init__(self,detailes):
        self.first_name=detailes["first_name"]
        self.last_name=detailes["last_name"]
        self.__phone=detailes["phone"]

    def get_phone(self):
        return self.__phone
    def set_phone(self,new_phone):
        if new_phone[0:3]=="+91":
            self.__phone=new_phone
            return "sucess"
        else:
            return "invalid"
detailes={
"first_name":"raja",
"last_name":"simha",
"phone":"+91924234324"

}

preson=Person(detailes)
print(preson.get_phone())
print(preson.set_phone("+94324234"))