import os

init_board = [['.','.','.'],['.','.','.'],['.','.','.']]
ABC = ["A","B","C"] 
A123 = ["1","2","3"]

a_len_init_board = len(init_board)

def game_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ","   ".join(A123)) 
    for i in range(a_len_init_board):
        print(ABC[i],' | '.join(init_board[i]))
        if i < 2:
            print(" ---+---+---")
    print()

def assign(row, column):
    row = row.upper()
    if row in ABC:
        if column in A123:
            return (ABC.index(row), A123.index(column))
        else:
            return False
    else:
        return False

def mark_the_spot(spot, mark):
    a = int(spot[0])
    b = int(spot[1])
    init_board[a][b] = mark
  
def win_set():
    win_set = []
    for i in init_board:
        win_set.append(set(i))

    for i in range(0,3):
        col = [init_board[0][i],init_board[1][i],init_board[2][i]]
        win_set.append(set(col))

    diag1 = []
    for i in range(0,3):
        diag1.append(init_board[i][i])
    win_set.append(set(diag1))
    
    diag2 = []
    for i in range(0,3):
        diag2.append(init_board[i][2-i])
    win_set.append(set(diag2))

    return win_set

def check_for_winners(win_set):
    x = set("X")
    o = set("O")
    
    if x in win_set:
        return True
    elif o in win_set:
        return True
    else:
        return False

def check_if_full():
    symbols = []
    for i in range(0,3):
        for j in range(0,3):
            symbols.append(init_board[i][j])
    if "." in symbols:
        return False
    else:
        return True

def moves_available(init_board):
    avail_moves = []
    for i in range(0,3):
        for j in range(0,3):
            if init_board[i][j] == ".":
                avail_moves.append([i, j])
    return avail_moves

def best_move(mark):
    avail_moves = moves_available(init_board)
    if mark == "X":
        best_score = -100
        for move in avail_moves:
            mark_the_spot(move, mark)
            score = minimax(init_board, 0, False)
            mark_the_spot(move, ".")
            if score > best_score:
                best_score = score
                chosen_move = move
        return chosen_move
    elif mark == "O":
        best_score = 100
        for move in avail_moves:
            mark_the_spot(move, mark)
            score = minimax(init_board, 0, True)
            mark_the_spot(move, ".")
            if score < best_score:
                best_score = score
                chosen_move = move
        return chosen_move

def minimax(init_board, depth, is_maxin):
    a = win_set()
    avail_moves = moves_available(init_board)
    if is_maxin == True:
        if check_for_winners(a) == True:
            return -10
        elif check_if_full() == True:
            return 0
        else:
            best_score = -100
            mark = "X"
            for move in avail_moves:
                mark_the_spot(move, mark)
                score = minimax(init_board, depth+1, False)
                mark_the_spot(move, ".")
                best_score = max(score, best_score)
            return best_score - depth
    if is_maxin == False:
        if check_for_winners(a) == True:
            return 10
        elif check_if_full() == True:
            return 0
        else:
            best_score = 100
            mark = "O"
            for move in avail_moves:
                mark_the_spot(move, mark)
                score = minimax(init_board, depth+1, True)
                mark_the_spot(move, ".")
                best_score = min(score, best_score)
            return best_score + depth

def game_play():
    counter = 1
    in_list = []

    while True:
        if counter % 2 == 1:
            mark = "X"
        else:
            mark = "O"
            
        game_board()

        print(f'{mark} player turn!!\n')
        coords = input("your move: e.g A1 or B2 \n")
        
        if len(coords) < 2:
            continue
        
        elif assign(coords[0],coords[1]) == False:
            continue
        
        place = assign(coords[0],coords[1])
        
        if place in in_list:
            print("Already choosen")
            continue
        else:
            in_list.append(place)
                
        mark_the_spot(place,mark)

        a = win_set()

        counter += 1
        
        if check_for_winners(a) == True:
            
            game_board()
            print(f'congratulation {mark} won\n')

            break
        elif check_if_full() == True:
            game_board()
            print(f'Unfortunately it is a draw')
            break
        else:
            continue

def single_player():
    counter = 0
    in_list = []

    while True:
        if counter % 2 == 0:
            mark = "X"
            game_board()
            print(f'{mark} player turn!!\n')
            coords = input("your move: e.g A1 or B2 \n")
            if len(coords) < 2:
                continue
            elif assign(coords[0],coords[1]) == False:
                continue
            place = assign(coords[0],coords[1])
            if place in in_list:
                print("Already choosen")
                continue
            else:
                in_list.append(place)        
            mark_the_spot(place,mark)
            a = win_set()
            counter += 1
            if check_for_winners(a) == True: 
                game_board()
                print(f'congratulation {mark} won\n')
                break
            elif check_if_full() == True:
                game_board()
                print('Unfortunately it is a draw')
                break
            else:
                continue
        else:
            mark = "O"
            choice = best_move(mark)
            mark_the_spot(choice, mark)
            in_list.append(tuple(choice))
            a = win_set()
            counter += 1
            a = win_set()
            if check_for_winners(a) == True:
                game_board()
                print(f'unfortunately you lost')
                break
            elif check_if_full() == True:
                game_board()
                print('its a tie')
                break
            else:
                continue

def main():
    a = input('''choose:
    1 for singleplayer
    2 for multiplayer\n''')
    if a == "1":
        single_player()
    elif a == "2":
        game_play()


if __name__ == "__main__":
    main()