import datetime
import string

birthday = {
    'apple fruit':(datetime.datetime())
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for items in birthday.keys():
    print(string.capwords(items))
while True:
    ask = input("Do you want to search or input?")
    if ask.isalpha():
        ask = ask.lower()
        if "input" in ask:
            name = input("What is your name? ")
            DD = int(input("Please enter your day of birth accordingly?\nDate: "))
            MM = int(input("Month: "))
            YY = int(input("Year: "))
            try:
                b_day = datetime.datetime(YY,MM,DD)
                birthday[(name.lower())] = b_day
            except TypeError:
                print("Invalid entry!")
        elif "search" in ask:
            search = input("Who's birthday do you want to look up?")
            if search in birthday:
                bday = birthday[search]
                lDD = bday.strftime("%d")
                lMM = bday.strftime("%m")
                lYY = bday.strftime("%Y")
                print(f"{string.capwords(search)}'s birthday is bday {lDD}/{lMM}/{lYY} ")
        elif "exit" in ask:
            break
        else:
            print("Invalid entry!")
    else:
        print("Invalid entry")
