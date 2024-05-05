import random
def board(x, y):
    print(
        f"{'X' if x[0] else ('O' if y[0] else 0)} | {'X' if x[1] else ('O' if y[1] else 1)} | {'X' if x[2] else ('O' if y[2] else 2)} ")
    print("--|---|---")
    print(
        f"{'X' if x[3] else ('O' if y[3] else 3)} | {'X' if x[4] else ('O' if y[4] else 4)} | {'X' if x[5] else ('O' if y[5] else 5)} ")
    print("--|---|---")
    print(
        f"{'X' if x[6] else ('O' if y[6] else 6)} | {'X' if x[7] else ('O' if y[7] else 7)} | {'X' if x[8] else ('O' if y[8] else 8)} ")


def sum(a, b, c):
    return a + b + c


def check(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            return 0
        result = [xState[i] + zState[i] for i in range(len(xState))]
        all_one = all(element == 1 for element in result)
        if all_one:
            return 2
    return -1

def opponent_wining_condition(xopponent,zopponent):
    magic_square = [8, 3, 4, 1, 5, 9, 6, 7, 2]
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        # Checking Wheather Opponent will Win
        if sum(xopponent[win[0]], xopponent[win[1]], xopponent[win[2]]) == 2:
            total = 0
            for i in win:
                if xopponent[i] == 1:
                    value = magic_square[i]
                    total = total + value
            wining_position = 15 -total
            index = magic_square.index(wining_position)
            if zopponent[index] == 1:
                continue
            else:
                zopponent[index] = 1
                return xopponent,zopponent
    return 1
def system_wining_condition(xSystem,zSystem):
    magic_square = [8, 3, 4, 1, 5, 9, 6, 7, 2]
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        # Checking Wheather System can Win
        if sum(zSystem[win[0]], zSystem[win[1]], zSystem[win[2]]) == 2:
            total_sys = 0
            for i in win:
                if zSystem[i] == 1:
                    value = magic_square[i]
                    total_sys = total_sys + value
            wining_position = 15 - total_sys

            index = magic_square.index(wining_position)
            if xSystem[index] == 1:
                continue
            else:
                zSystem[index] = 1
                return xSystem, zSystem
    return 1
def System_play(xplay,zplay):
    opponent=opponent_wining_condition(xplay,zplay)
    if opponent==1:
        system=system_wining_condition(xplay,zplay)
        if system==1:
            position=[]
            for i in range(0,len(zplay)):
                if zplay[i]==0:
                    position.append(i)
            for i in range(0,len(xplay)):
                if zplay[i]==1:
                    if i in position:
                        position.remove(i)
            random_picking=random.choice(position)
            zplay[random_picking]=1
            zwin=zplay
        else:
            zwin = system[1]
    else:
        zwin = opponent[1]
    return xplay,zwin

if __name__ == "__main__":
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==== Tic Tac Toe ====-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    player = input("Enter the  Player Name : ")
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("Welcome to Tic tac Toe")
    while (True):
        while (True):
            board(xState, zState)
            if (turn == 1):
                print(f"---------- {player} Turn ----------")
                value = int(input("Please enter the value :"))
                if xState[value] == 1 or zState[value] == 1:
                    print("\nThe Value is already enter")
                    break
                xState[value] = 1
                turn = 0
            else:
                print(f"---------- System Turn ----------")
                xState,zState=System_play(xState,zState)
                turn = 1
            cwin = check(xState, zState)
            if (cwin != -1):
                print(
                    "---------------------------------------------- MATCH OVER ------------------------------------------------")
                board(xState, zState)
            if (cwin == 1):
                print(f"\n\n============================ {player} Won ===================")
                exit()
            elif (cwin == 0):
                print(f"\n\n============================ System Won ===================")
            elif (cwin == 2):
                print(f"\n\n============================ It's a Draw ===================")
                exit()