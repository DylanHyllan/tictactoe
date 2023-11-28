board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

# funktion för hur brädan ser ut när den printas
def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("Var snäll och välj en position för x mellan 1 och 9\n")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print('Förlåt, denna plats är redan tagen')
            else:
                print('Var snäll och skriv ett numemr från 1 till 9')

        except:
            print('Var snäll och skriv in ett nummer')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Välkommen til spelet!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("Förlåt du förlora!")
            break

        if not(IsWinner(board , 'X')):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O' , move)
                print('Datorn placerade o i positionen' , move , ':')
                printBoard(board)
        else:
            print("Du vann!")
            break




    if isBoardFull(board):
        print("Lika spel")

while True:
    x = input("Vill du spela? Tryck j for ja eller n för nej (j/n)\n")
    if x.lower() == 'j':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break