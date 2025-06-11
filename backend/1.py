#creating api requests
#postman api
#  #
import requests


print("words related to something that start with the letter something	")
word=input("enter word: ")
letter=input("enter letter: ")

request=requests.get(f"https://api.datamuse.com/words?ml={word}&sp={letter}*&max=10")
content=request.json()
# print(content)
print(request.status_code)
for i in range(5):
    print(content[i]["word"])