import random
def cowandbull(ran_num,user_num):
    ran_num,user_num = str(ran_num),str(user_num)
    cow = 0
    bull = 0
    optionleft = list(ran_num)
    guessleft = list(user_num)
    for ran_dig,user_dig in zip(ran_num,user_num):
        if ran_dig == user_dig:
            cow += 1
            optionleft.remove(user_dig)
            guessleft.remove(user_dig)
    for user_dig in guessleft:
        if user_dig in optionleft:
            bull += 1
            optionleft.remove(user_dig)
    cow_sen = "cow" if cow < 2 else "cows"
    bull_sen = "bull" if bull < 2 else "bulls"
    print(f"{cow} {cow_sen}, {bull} {bull_sen}")

if __name__ == "__main__":
    playing = True
    target = random.randint(1000,9999)
    guess = 0
    print("Welcome to the Cows and Bulls Game!")
    while playing:
        player = input("Enter a number:")
        if player == "exit":
            break
        elif player == "number":
            print(target)
        elif player.isdigit() == False or len(player) != 4:
            print("Please Enter 4 digit number")
        elif int(player) == int(target):
            playing = False
            print("Congratulations! You win!")
            print(f"The number is {target}. Your guess: {guess}")
            break
        else:
            guess += 1
            cowandbull(target,player)
            
