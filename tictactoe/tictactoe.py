cell = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


def printCell(cell):
    """Отображает Игровое поле"""
    print(cell[0] + " | " + cell[1] + " | " + cell[2])
    print("---------")
    print(cell[3] + " | " + cell[4] + " | " + cell[5])
    print("---------")
    print(cell[6] + " | " + cell[7] + " | " + cell[8])


def playerInput(cell):
    """Просит игрока выбрать ячейку """
    inp = int(input("Select a spot 1-9: "))
    if cell[inp-1] == "-":
        cell[inp-1] = currentPlayer
    else:
        print("This cell is occupied! Choose another one!")


def checkHorizontle(cell):
    """Ищет победителя по Горизонтали"""
    global winner
    if cell[0] == cell[1] == cell[2] and cell[0] != "-":
        winner = cell[0]
        return True
    elif cell[3] == cell[4] == cell[5] and cell[3] != "-":
        winner = cell[3]
        return True
    elif cell[6] == cell[7] == cell[8] and cell[6] != "-":
        winner = cell[6]
        return True


def checkRow(cell):
    """Ищет победителя по строке"""
    global winner
    if cell[0] == cell[3] == cell[6] and cell[0] != "-":
        winner = cell[0]
        return True
    elif cell[1] == cell[4] == cell[7] and cell[1] != "-":
        winner = cell[1]
        return True
    elif cell[2] == cell[5] == cell[8] and cell[2] != "-":
        winner = cell[3]
        return True


def checkDiag(cell):
    """Ищет победителя по Диогонали"""
    global winner
    if cell[0] == cell[4] == cell[8] and cell[0] != "-":
        winner = cell[0]
        return True
    elif cell[2] == cell[4] == cell[6] and cell[4] != "-":
        winner = cell[2]
        return True


def checkIfWin(cell):
    """Проверяет победу"""
    global gameRunning
    if checkHorizontle(cell):
        printCell(cell)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(cell):
        printCell(cell)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(cell):
        printCell(cell)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(cell):
    """Проверяет ничью"""
    global gameRunning
    if "-" not in cell:
        printCell(cell)
        print("Draw!")
        gameRunning = False


def switchPlayer():
    """Смена Игрока, Х всегда первый"""
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


while gameRunning:
    printCell(cell)
    playerInput(cell)
    checkIfWin(cell)
    checkIfTie(cell)
    switchPlayer()

