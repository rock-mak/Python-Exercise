import random
hangman_file = open('sowpods.txt')
target = random.choice(hangman_file.readlines())

def word_len(word):
    return "_ " * (len(word)-1)

def hangman(guess,word):
    word = enumerate(word)
    num_list = []
    for i,v in word:
        if guess in v:
            num_list.append(i)
    return num_list
            
playing = True
count = 6
print('Welcome to hangman!')
print(target)
show = word_len(target)

while playing:
    if count == 0:
        print(f"Chance left: {count}\nBetter luck next time!")
        break
    print(show, "  Guess chances: ", count)
    user_ = input("Guess your letter: ")
    
    if user_.isalpha() and len(user_) == 1:
        user_ = user_.upper()
        if user_ in target:
            for i in hangman(user_,target):
                show = list(show.replace(' ',''))
                show[int(i)] = user_
                show = ' '.join(show)
                if show.replace(" ",'') == target:
                    print(f"Congratulation! Tries left: {count}")
                    playing = False
        else:
            count -= 1
            print("Incorrect!")
    else:
        print("Invalid entry!")
    
again = input("Do you want to play again?")
if "YES" or 'yes' in input:
    playing = True
else:
    print("Thank you for playing!")
