import requests

userInput = input('enter your name')
userInput2 = input('enter your lasName')
userInput3 = input('enter your email')
userInput4 = int(input('enter your age'))

myObj = {
    'name': userInput,
    'lastName': userInput2,
    'email': userInput3,
    'age': userInput4
}

url = 'https://dash-6248c-default-rtdb.firebaseio.com/users.json'

requests.post(url, json=myObj)