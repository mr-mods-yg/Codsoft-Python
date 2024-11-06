import sys
import string
import random
from tabulate import tabulate

passwords = []
print("Password Generator")
noOfSamples = 5
length = int(input("Enter length of password: "))
if(length<0):
    print("error : negative values not allowed!")
    sys.exit(0)
print("default option: Y")

trueCond = ['', 'Y']
numbers = True if input("include numbers :(Y/N)") in trueCond else False
lowerCaseLetters = True if input("include lowercase letters :(Y/N)") in trueCond else False
upperCaseLetters = True if input("include uppercase letters :(Y/N)") in trueCond else False
punctuations = True if input("include punctuations :(Y/N)") in trueCond else False

userPasswordChoicePattern = ""

if(numbers):
    userPasswordChoicePattern += string.digits
if(lowerCaseLetters):
    userPasswordChoicePattern += string.ascii_lowercase
if(upperCaseLetters):
    userPasswordChoicePattern += string.ascii_uppercase
if(punctuations):
    userPasswordChoicePattern += string.punctuation

for i in range(noOfSamples):
    password = ''
    for j in range(length):
        password+=random.choice(userPasswordChoicePattern)
    passwords.append(password)
print()
print(tabulate([[passwd] for passwd in passwords], headers=["Generated Passwords"]))