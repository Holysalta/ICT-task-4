from random import randint

def generate_bingo_card():    
    bingo_card = {
        'B':[None] * 5,
        'I':[None] * 5,
        'N':[None] * 5,
        'G':[None] * 5,
        'O':[None] * 5
    }
    k = 15
    l = 1
    for i in bingo_card:
        
        for j in range(5):
            bingo_card[i][j] = randint(((l * k) - 15) + 1, k * l)
        l+=1
    return bingo_card
def display_bingo_card(bingo_card):
    table = ""
    for key, value in bingo_card.items():
        table+=key + " "
    table += '\n' 
    for key, value in bingo_card.items():
        for i in range(len(bingo_card[key])):
            table+=str(bingo_card[key][i]) + " "
        table+='\n'
    print(table)
        
bingo_card = generate_bingo_card()
def isBingoCardWon(bingo_card):
    sum_by_horizontally = [0] * 5
    sum_by_vertically = [0] * 5
    sum_by_diagonally = 0
    i = 0
    b = False
    for key, value in bingo_card.items():
        sum_by_horizontally[i] = sum(value)
        for j in range(len(value)):
            if(i==j):
                sum_by_diagonally += value[j]
        i+=1
    arr = []
    for key, value in bingo_card.items():
        arr.append(value)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(i==j):
                sum_by_vertically[i] += arr[i][j]
    return b
bb = generate_bingo_card()
display_bingo_card(bb)
isBingoCardWon(bb)