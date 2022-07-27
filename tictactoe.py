"""
Tic Tac Toe Player
"""

from json.encoder import INFINITY
import math

X = "X"
O = "O"


EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1

    if xCount == oCount:
        return X
    elif xCount == oCount + 1:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []

    for i in range (3):
        for j in range (3):
            if board[i][j] == None:
                actions.append((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardDemo = board
    boardDemo[action[0]][action[1]] = player(board)
    return boardDemo


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    switch = False

    for i in range(3):
        for j in range(3):
            if(board[i][j] == None):
                switch = True
    
    if not switch:
        return True

    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    Max = -math.inf
    Min = math.inf

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];