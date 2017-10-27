from random import *


def printBoard(liste, lenLine=3):
    '''
    liste : list of num or string
    lenLine : length of the desired board
    return : line to be printed to have the board
    '''
    counter = 1
    line = ''
    #  set a counter and add \n every lenLine
    for char in liste:
        if counter % lenLine == 0:
            line += '| ' + str(char) + ' |' + '\n'
        else:
            line += '| ' + str(char) + ' '
            pass
        counter += 1
    return(line)


def playersNumberName():
    '''
    input : none
    return : list with name(s) of player(s)
    '''
    playersNumber = '0'
    while playersNumber != '1' and playersNumber != '2':
        playersNumber = input("How many to play (choose 1 or 2 players) ?")
    #  control if number of players is correct :
    if playersNumber == '2':
        name1 = input("What's your name player 1 ?")
        name2 = input("What's your name player 2 ?")
        names = [name1, name2]
        return(names)
    else:
        name = input("Who cares, but what's your name ?")
        return([name])


def play(player, liste, marker):
    '''
    player : human or computer
    liste  : list of cases
    return : list of played cases
    take player or computer input, check if a int, in the good range, and if
    the case is empty in the liste. Marker is defined by an external counter.
    '''
    # set game for computer player
    if player == 'I':
        # check if the case is empty
        marker = 'O'
        check = False
        while not check:
            case = randint(0,8)
            if liste[case] == '.':
                liste[case] = marker
                check = True
    else:
        case = ''
        check = False
        # check if number entered by user, in the good range
        while not check:
            case = input('\n' + player + ', choose an empty box (1 to 9) :\n')
            if case.isdigit():
                if int(case) in range(1, 10):
                    case = int(case) - 1
                    if liste[case] == '.':
                        liste[case] = marker
                        check = True
    return(liste)


def checkWin(liste, counter, name1='You', name2='I'):
    '''
    list : list of played case
    name : name of players
    counter : external counter to check if draw
    return : win, lost or draw status depending of an external counter
    '''
    winList = ['123', '456', '789', '147', '258', '369', '159', '357']
    resultX = ''
    resultO = ''

    for i in range(0, 9):
        if liste[i] == 'X':
            # add 1 to index iot compare to win list !!!!
            resultX += str(i+1)
        elif liste[i] == 'O':
            resultO += str(i+1)
    # check if one of the players have won
    for win in winList:
        if win in resultX:
            return(name1 + ' win !')
        elif win in resultO:
            return(name2 + ' win !')
        # set counter to 10 to be sure there is no win on last turn
        elif counter == 10:
            return("It's a draw !")


def printGame(names, intro):
    if intro == 'yes':
        print('\nPython TicTacToe Game\n=====================')
        if len(names) == 2:
            print("Ok, let's get to Rumble " + names[0] + " and " + names[1] + " !\n")
        else:
            print("Ok, let's fight, I'll crush you 'dear' " + names[0]
                    + " !\nYou start, but I keep the O\n")
    print('Reference Board\n')
    print(printBoard(example))
    if len(names) == 2:
        print('The Battlefield\n')
    else:
        print('Your board of defeat\n')
    print(printBoard(board))


##############################
example = range(1, 10)
text = '. '*9
emptyBoard = text.split()

board = emptyBoard
counter = 0

names = playersNumberName()
printGame(names, 'yes')

if len(names) == 2:
    player1 = names[0]
    player2 = names[1]
else:
    player1 = 'You'
    player2 = 'I'

while checkWin(board, counter) is None:
    for player in [player1, player2]:
        # check parity of counter to set marker
        if counter % 2 == 0:
            marker = 'X'
        else:
            marker = 'O'
        # players play and print the board after each play
        board = play(player, board, marker)
        printGame(names, 'no')
        # check if one of the player has won
        if checkWin(board, counter) is None:
            # if not, add 1 to counter to count the played turn
            counter += 1
            # check if it's the last turn
        else:
            # if there is a winner, break the loop and print him
            break
        if counter == 9:
            # if so, without a winner, add 1 to counter iot print the draw
            counter += 1
            # break the loop and print the draw
            break
print(checkWin(board, counter, player1, player2))
