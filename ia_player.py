from models.move import Move

class IaPlayer:
  
  import time

  def getMovementValue(self, color, isMyTurn, board, roundNum, fatherValue):

    validMoves = board.valid_moves(color)

    now = self.time.time()
    time = now - self.start
    
    if len(validMoves) <= 0 or roundNum >= self.maxRounds or time > 2.9 :
      return self.getMinMaxValue(board)
    else:
      movValue = None
      colorTemp = '@'
      if color == '@':
        colorTemp = 'o'

      for move in  validMoves:
        boardClone = board.get_clone()
        boardClone.play(move, color)

        movTempValue = self.getMovementValue(colorTemp, isMyTurn, boardClone, roundNum + 1, movValue)

        if movValue == None or (isMyTurn * movValue < isMyTurn * movTempValue):
          movValue = movTempValue
          if fatherValue != None and (isMyTurn * fatherValue < isMyTurn * movValue):
            return movTempValue;

      return movValue

  def getMinMaxValue(self, board):
    score = self.score(board)
    if self.color == 'o':
      return score[0] - score[1]
    else:
      return score[1] - score[0]

  def score(self, board):
    white = 0
    black = 0
    for i in range(1, 9):
      for j in range(1, 9):
        fator = 1
        if i == 1 or  i == 8 or j == 1 or j == 8:
          fator = 3
        if board.board[i][j] == 'o':
          white += (1 * fator)
        elif board.board[i][j] == '@':
          black += (1 * fator)

    return [white, black]


  def __init__(self, color):
    self.color = color
    self.maxRounds = 10

  def play(self, board):
  
    validMoves = board.valid_moves(self.color)
    movValue = None
    myMove = None

    self.start = self.time.time()

    colorTemp = '@'
    if self.color == '@':
      colorTemp = 'o'

    for move in  validMoves:
      boardClone = board.get_clone()
      boardClone.play(move, self.color)
      movTempValue = self.getMovementValue(colorTemp, -1, boardClone, 1, movValue)
      if movValue == None or movValue < movTempValue:
        myMove = move
        movValue = movTempValue

    return myMove