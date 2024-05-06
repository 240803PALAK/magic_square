import random

def sum(a, b, c):
    return a + b + c


def check(xState, zState):
    result = [xState[i] + zState[i] for i in range(len(xState))]
    all_one = all(element == 1 for element in result)
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            return 1,win
        elif sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            return 0,win
        elif all_one:
            return 2," "
    return -1," "

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
    system = system_wining_condition(xplay, zplay)
    if system==1:
        opponent=opponent_wining_condition(xplay,zplay)
        if opponent==1:
            position=[]
            for i in range(0,len(zplay)):
                if zplay[i]==0 and xplay[i]==0:
                    position.append(i)
            for i in range(0,len(xplay)):
                if zplay[i]==1:
                    if i in position:
                        position.remove(i)
            random_picking=random.choice(position)
            zplay[random_picking]=1
            zwin=zplay
        else:
            zwin = opponent[1]
    else:
        zwin = system[1]
    return xplay,zwin

