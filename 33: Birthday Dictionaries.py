import datetime

birthday = {}

def add_ele(dic, name, b_day):
    dic[name] = b_day

print("Welcome to the birthday dictionary. We know the birthdays of:")
try:
    for key, value in birthday:
        print(key)
except ValueError:
    return None
while True:
    ask = input("Do you want to look up or input? ")
    if "input" in ask.lower():
        name = input("What is your name? ")
        b_day = input("What is your day of birth? ")
        add_ele(birthday, name, b_day)
    elif "look up" in ask.lower():
        lookup = input
