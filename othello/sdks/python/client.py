#!/usr/bin/python

import sys
import json
import socket

def get_move(player, board):
  # TODO determine valid moves
  # TODO determine best move
  print("Board:"+str(board))
  print("Player:"+str(player))
  me = player
  #get valid move socket
  validMoveList = getValidMoves(board, me)
  markCorners(validMoveList)
  print("Valid Moves: " + str(validMoveList))
  # make a corner move if they exist
  for gamePiece in validMoveList: # get the game piec
    for choice in gamePiece: #get the move on that piece that is valid
        if(choice[2] is 1):
            return choice[0]

  print("Valid Moves: " + str(validMoveList))
  return [4, 2] # (y, x) or (col, row)

def markCorners(validMoveList):
    '''
        mark good corners and bad corners and not corners
    '''
    #good corner list
    goodCorners = [[0,0],[0,7],[7,7],[7,0]]
    print(type(goodCorners))
    #bad corner list
    badCorners = [[0,1],[1,1],[1,0],[0,6],[1,6],[1,7],[6,0],[6,1],[7,1],[7,6],[6,6],[6,7]]
    for gamePiece in validMoveList: # get the game piece
        for choice in gamePiece: #get the move on that piece that is valid
            if(choice[0] in badCorners): # mark as bad corner
                goodCor = 0
                choice.append(goodCor)
            elif(choice[0] in goodCorners): # mark as good corner
                goodCor = 1
                choice.append(goodCor)
            else: #nothing but its even across all
                goodCor = 3
                choice.append(goodCor)

def getValidMoves(board, me):
    '''A list or single value of all the possible moves we could make'''

    validMoves = []
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if(board[row][col] is me):  # is location us
                validMoves.append(nexToPlayer(me, row, col, board))
    return validMoves

def nexToPlayer(me, row, col, board):
    '''
        This will search all directions from our current
        spot to find all possible next valid moves for that spot
    '''
    #check up
    validMoves = []
    if(row is not 0):
        #check until we hit the end of a string of enemys
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        boolFoundEnemy = False
        #while(we arent at a border and the next spot is not empty and we havent yet run into ourselves)
        while(rowCopy is not 0 and board[rowCopy-1][col] is not 0 and not boolFoundMe):
            rowCopy = rowCopy - 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][col] is me): # if we found ourselves make it stop calculating becaseu tahts a new poitn to check from not our job righ tnow
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0): # if we never hit ourselves and we are flipping more than 0 add it as a spot
            validMoves.append([[rowCopy-1,col],enemyCount])
    #check down
    if(row is not 7):
        #check until we hit the end of enemey
        rowCopy = row
        enemyCount = 0
        boolFoundMe = False
        while(rowCopy is not 7 and board[rowCopy+1][col] is not 0 and not boolFoundMe):
            rowCopy = rowCopy + 1
            enemyCount = enemyCount + 1
            if(board[rowCopy][col] is  me):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append([[rowCopy+1,col],enemyCount])
    #left
    if(col is not 0):
        colCopy = col
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 0 and board[row][colCopy-1] is not 0 and not boolFoundMe):
            colCopy = colCopy - 1
            enemyCount = enemyCount + 1
            if(board[row][colCopy] is  me):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append([[row,colCopy-1],enemyCount])

    #check right
    if(col is not 7):
        colCopy = col
        enemyCount = 0
        boolFoundMe = False
        while(colCopy is not 7 and board[row][colCopy+1] is not 0 and not boolFoundMe):
            colCopy = colCopy + 1
            enemyCount = enemyCount + 1
            if(board[row][colCopy] is  me):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append([[row,colCopy+1],enemyCount])

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
            if(board[rowCopy][colCopy] is  me):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append([[rowCopy-1,colCopy-1],enemyCount])
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
            if(board[rowCopy][colCopy] is  me):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append([[rowCopy+1,colCopy-1],enemyCount])
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
            if(board[rowCopy][colCopy] is  me):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append([[rowCopy-1,colCopy+1],enemyCount])
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
            if(board[rowCopy][colCopy] is  me):
                boolFoundMe = True
        if(not boolFoundMe and enemyCount is not 0):
            validMoves.append([[rowCopy+1,colCopy+1],enemyCount])

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
