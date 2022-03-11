from datetime import datetime
import random

def printCoordBoard():

    print("\nCOORDENADAS DO TABULEIRO\n")
    print("(x=0 y=2) | (x=1 y=2) | (x=2 y=2)")
    print("----------|-----------|----------")
    print("(x=0 y=1) | (x=1 y=1) | (x=2 y=1)")
    print("----------|-----------|----------")
    print("(x=0 y=0) | (x=1 y=0) | (x=2 y=0)")

def printBoard(board):

    print("\nTABULEIRO ATUAL\n")

    for i in range(len(board) - 1, -1, -1):

        if i != len(board) - 1:
            print("---|---|---")

        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]}")

def game():

    id = datetime.now().strftime('%Y-%m-%d-%H-%M')

    firstPlayer = "X" if random.randint(0,9) % 2 == 0 else "O"

    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    movements = []

    game = {
        "id" : id,
        "firstPlayer" : firstPlayer,
        "board" : board,
        "movements" : movements
    }

    return game

def gameMovement(game):

    # Define jogador
    if len(game["movements"]) == 0:
        player = game["firstPlayer"]

    else:
        player = "O" if game["movements"][-1]["player"] == "X" else "X"

    print(f"\nVez do jogador {player}.")

    # Lê coordenadas
    x = int(input("Digite a coordenada de x: "))
    y = int(input("Digite a coordenada de y: "))

    # Contorna possíveis erros
    if x < 0 or x > 2 or y < 0 or y > 2:
        print("\nCoordenada inválida.")
        return
    
    if game["board"][y][x] != ' ':
        print("\nCoordenada já foi preenchida.")
        return

    # Marca jogada
    game["board"][y][x] = player

    #Registra dados
    position = {
        "X": x,
        "y": y
    }

    movement = {
        "player": player,
        "position": position
    }

    game["movements"].append(movement)

    return 200

def gameStatus(board, amountMovements):

    statusCode = ""
    winner = ""

    # Verifica linhas e colunas
    for i in range(0, len(board)):

        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][1] != " ":
            statusCode = 1
            winner = board[i][1]
        
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[1][i] != " ":
            statusCode = 1
            winner = board[1][i]

    # Caso não se tenha encontrado ganhador
    if statusCode == "":

        # Verifica diagonais
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != " ") or (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != " "):
            statusCode = 1
            winner = board[1][1]

        # Identifica velha
        elif amountMovements == 9:
            statusCode = 2

        # Jogo ainda em andamento
        else: return 0
    
    status = {
        "msg" : "Partida finalizada, ",
        "winner" : "Draw" if statusCode == 2 else winner,
        "detail": "deu velha!" if statusCode == 2 else f" o jogador {winner} venceu!"
    }

    return status

games = []

while True:

    answer = input("\nIniciar nova partida? S/N: ")

    if answer != "S":
        print("Programa finalizado com sucesso.")
        break
    
    actualGame = game()

    while True:

        printCoordBoard()
        printBoard(actualGame["board"])

        sucesso = gameMovement(actualGame)

        if sucesso == 200:
            status = gameStatus(actualGame["board"], len(actualGame["movements"]))

            if status != 0:
                print("\n" + status["msg"] + status["detail"])
                printBoard(actualGame["board"])
                break
        
    games.append(actualGame)
