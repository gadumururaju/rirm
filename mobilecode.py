import re
while True:
    num=input("enter your mobile number:")
    pattren=re.compile("\+1?\s?-?\(?[1-2]{3}\)?\s?.?-?[4-6]{3}\s?.?-?[7-9or0]{4}")
    if pattren.match(num):
        print("valid mobile number:")
        break
    else:
        print("invalid mobile number.please try again!")

