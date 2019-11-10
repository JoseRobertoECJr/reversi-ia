from models.move import Move

class IaPlayer:
  
  import time

  def getMovementValue(self, color, board, isMyTurn, roundNum, maxRounds):

    validMoves = board.valid_moves(color)

    now = self.time.time()
    time = now - self.start
    
    if len(validMoves) <= 0 or roundNum >= maxRounds or time > 2.9 :
      return isMyTurn * self.getMinMaxValue(board)
    else:
      movValue = None
      for move in  validMoves:
        boardClone = board.get_clone()
        boardClone.play(move, color)

        colorTemp = 'o'
        if color == colorTemp:
          colorTemp = '@'

        movTempValue = self.getMovementValue(colorTemp, boardClone,-isMyTurn, roundNum + 1, maxRounds)

        if movValue == None or (isMyTurn * movValue < isMyTurn * movTempValue):
          movValue = movTempValue

      return movValue

  def getMinMaxValue(self, board):
    score = board.score()
    if self.color == 'o':
      return score[0] - score[1]
    else:
      return score[1] - score[0]




  def __init__(self, color):
    self.color = color

  def play(self, board):
  
    validMoves = board.valid_moves(self.color)
    movValue = None
    myMove = None

    self.start = self.time.time()

    for move in  validMoves:
      boardClone = board.get_clone()
      boardClone.play(move, self.color)
      movTempValue = self.getMovementValue(self.color, boardClone, 1, 1, 10)
      if movValue == None or movValue < movTempValue:
        myMove = move
        movValue = movTempValue

    return myMove