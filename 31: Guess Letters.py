import random
hangman_file = open('sowpods.txt')
words = hangman_file.readlines()

def word_len(word):
    return "_ " * (len(word))

def hangman(guess,word):
    return [i for i,v in enumerate(word) if v == guess]
            
playing = True

print('Welcome to hangman!')

while playing:
    count = 6
    target = random.choice(words).strip().upper()
    show = word_len(target).strip()
    print(target)
    while count > 0:
        print(show, "  Guess chances: ", count)
        user_ = input("Guess your letter: ")
        if user_.isalpha() and len(user_) == 1:
            user_ = user_.upper()
            if user_ in target:
                for i in hangman(user_,target):
                    show_list = list(show.replace(' ',''))
                    show_list[i] = user_
                    show = ' '.join(show_list)
                if show.replace(" ",'') == target:
                    print(f"Congratulation! Tries left: {count}")
                    break
            else:
                count -= 1
                print("Incorrect!")
        else:
            print("Invalid entry!")
    if count == 0:
            print(f"Chance left: {count}\nBetter luck next time!\nThe word is {target}")
    
    again = input("Do you want to play again?")
    if "YES" or 'yes' not in input:
        print("Thank you for playing!")
        playing = False
