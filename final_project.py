from random import randrange
from wsgiref.validate import validator


def display_board(board):
    """
    La función acepta un parámetro el cual contiene el estado actual del tablero
    y lo muestra en la consola.
    """
    print(f"+-------+-------+-------+\n",
          f"|       |       |       |\n",
          f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n",
          f"|       |       |       |\n",
          f"+-------+-------+-------+\n",
          f"|       |       |       |\n",
          f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n",
          f"|       |       |       |\n",
          f"+-------+-------+-------+\n",
          f"|       |       |       |\n",
          f"|   {board[2][0]}   |   {board[2][1]}   |  {board[2][2]}    |\n",
          f"|       |       |       |\n",
          f"+-------+-------+-------+")

def enter_move(board):
    """
    La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    """
    validator = True
    while validator:
        try:
            move = int(input("Ingresa tu movimiento: "))
            if move < 1 or move > 9:
                print("Movimiento inválido. Por favor, intenta de nuevo.")
            else:
                for item in board:
                    if move in item:
                        index = item.index(move)
                        item[index] = "O"
                        draw_move(board)
                        validator = False
                else:
                    print("Ese cuadro ya está ocupado. Por favor, intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número.")

def victory_for(board, sign):
    """
    La función analiza el estatus del tablero para verificar si
    el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    """
    for row in board:
        if row.count(sign) == 3:
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False


def draw_move(board):
    """
    La función dibuja el movimiento de la máquina y actualiza el tablero.
    """
    display_board(board)
    if victory_for(board, "O"):
        print("¡Has ganado!")
        exit(0)
    elif victory_for(board, "X"):
        print("¡La máquina ha ganado!")
        exit(0)
    else :
        change_status = True
        while change_status:
            machine_move = randrange(1, 10)
            for item in board:
                if machine_move in item:
                    index = item.index(machine_move)
                    item[index] = "X"
                    display_board(board)
                    change_status = False
                    break
        enter_move(board)



board = [[1, 2, 3],
         [4, "X", 6],
         [7, 8, 9]]
display_board(board)
enter_move(board)


