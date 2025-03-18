import random

target = random.randint(1,9)
count = 0
playing = True

while playing:
    user_ = input("Guess a number (1-9) ")
    if user_.isdigit():
        user_ = int(user_)
        if 1 < user_ < 10:
            if user_ < target:
                count += 1
                print("too low")
            elif user_ > target:
                count += 1
                print("too high")
            elif user_ == target:
                print("exact7ly right")
                playing = False
        else:
            print("Please input a valid digit between 1-9 ")
            
    elif user_.lower() == "exit":
        playing = False
    else:
        print("Please input a valid digit between 1-9 ")

ans = input("Do you want to play again? ")
if "yes" in ans.lower():
    count = 0
    playing = True
else:
    print("Thanks for playing")
