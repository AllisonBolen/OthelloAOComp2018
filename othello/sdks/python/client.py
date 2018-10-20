#!/usr/bin/python

import sys
import json
import socket

def get_move(player, board):
  # TODO determine valid moves
  # TODO determine best move
  print("Board:"+str(board))
  print("Player:"+str(player))
  validMoveList = getValidMoves(board, player)
  print("Valid Moves: " + str(validMoveList))
  return [4, 2] # (y, x) or (col, row)

'''A list or single value of all the possible moves we could make'''
def getValidMoves(board, player):
    validMoves = []
    print("len:"+str(len(board))+"len row: "+ str(len(board[1])))
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if(board[row][col] is player):  # is location us
                print("Row:"+str(row)+"Col:"+str(col))
                validMoves.append(nexToPlayer(player, row, col, board))
    return validMoves

def nexToPlayer(player, row, col, board):
    '''
        This will search all directions from our current
        spot to find all possible next valid moves for that spot
    '''
    #check up
    validMoves = []
    if(row is not 0):
        print("check Up from:"+str(row)+""+str(col))
        #check until we hit the end of a string of enemys
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        boolFoundEnemy = False
        #while(we arent at a border and the next spot is not empty and we havent yet run into ourselves)
        while(rowCopy is not 0 and board[rowCopy-1][col] is not 0 and not boolFoundMe):
            rowCopy = rowCopy - 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][col] is player): # if we found ourselves make it stop calculating becaseu tahts a new poitn to check from not our job righ tnow
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0): # if we never hit ourselves and we are flipping more than 0 add it as a spot
            validMoves.append((rowCopy-1,col,enemyCount))
    #check down
    if(row is not 7):
        #check until we hit the end of enemey
        print("check DOWN from:"+str(row)+""+str(col))
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        while(rowCopy is not 7 and board[rowCopy+1][col] is not 0 and not boolFoundMe):
            rowCopy = rowCopy + 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][col] is  player):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append((rowCopy+1,col,enemyCount))
    #left
    if(col is not 0):
        colCopy = col
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 0 and board[row][colCopy-1] is not 0 and not boolFoundMe):
            colCopy = colCopy - 1
            enemyCount = enemyCount + 1
            if(board[row][colCopy] is  player):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append((row,colCopy-1,enemyCount))

    #check right
    if(col is not 7):
        colCopy = col
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 7 and board[row][colCopy+1] is not 0 and not boolFoundMe):
            colCopy = colCopy + 1
            enemyCount = enemyCount + 1
            if(board[row][colCopy] is  player):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append((row,colCopy+1,enemyCount))

    #check dia up left
    if(row is not 0 and col is not 0):
        colCopy = col
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 0 and rowCopy is not 0 and board[rowCopy-1][colCopy-1] is not 0 and not boolFoundMe):
            colCopy = colCopy - 1
            rowCopy = rowCopy - 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][colCopy] is  player):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append((rowCopy-1,colCopy-1,enemyCount))
    #check dia down left
    if(row is not 7 and col is not 0):
        colCopy = col
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 0 and rowCopy is not 7 and board[rowCopy+1][colCopy-1] is not 0 and not boolFoundMe):
            colCopy = colCopy - 1
            rowCopy = rowCopy + 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][colCopy] is  player):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append((rowCopy+1,colCopy-1,enemyCount))
    #check dia up right
    if(row is not 0 and col is not 7):
        colCopy = col
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 7 and rowCopy is not 0 and board[rowCopy-1][colCopy+1] is not 0 and not boolFoundMe):
            colCopy = colCopy + 1
            rowCopy = rowCopy - 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][colCopy] is  player):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append((rowCopy-1,colCopy+1,enemyCount))
    #check dia down right
    if(row is not 7 and col is not 7):
        colCopy = col
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 7 and rowCopy is not 0 and board[rowCopy+1][colCopy+1] is not 0 and not boolFoundMe):
            colCopy = colCopy + 1
            rowCopy = rowCopy + 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][colCopy] is  player):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append((rowCopy+1,colCopy+1,enemyCount))

    #return all the values that we found we can hit
    return validMoves

def prepare_response(move):
  response = '{}\n'.format(move).encode()
  print('sending {!r}'.format(response))
  return response

if __name__ == "__main__":
  port = int(sys.argv[1]) if (len(sys.argv) > 1 and sys.argv[1]) else 1337
  host = sys.argv[2] if (len(sys.argv) > 2 and sys.argv[2]) else socket.gethostname()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    sock.connect((host, port))
    while True:
      data = sock.recv(1024)
      if not data:
        print('connection to server closed')
        break
      json_data = json.loads(str(data.decode('UTF-8')))
      board = json_data['board']
      maxTurnTime = json_data['maxTurnTime']
      player = json_data['player']
      print(player, maxTurnTime, board)

      move = get_move(player, board)
      response = prepare_response(move)
      sock.sendall(response)
  finally:
    sock.close()
