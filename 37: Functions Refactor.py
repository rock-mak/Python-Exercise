def board(num):
    top = " ----" 
    mid = ("|    ")

    for i in range(num):
        print(top*num)
        print((mid*num)+'|')
    print(top*num)
    
ask = int(input("What size do you want? "))
board = board(ask)
