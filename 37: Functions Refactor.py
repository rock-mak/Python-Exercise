def board(num):
    top = " ----" 
    mid = ("|    ")
    matrix = []
    for i in range(num):
        matrix.append(top*num)
        matrix.append((mid*num)+'|')
    matrix.append(top*num)
    return matrix
    
ask = int(input("What size do you want? "))
board = board(ask)
for i in board:
    print(i)
