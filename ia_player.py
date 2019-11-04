from models.move import Move

class IaPlayer:
  
  def getMovementValue(self, color, board, isMyTurn, roundNum, maxRounds):

    validMoves = board.valid_moves(color)

    if len(validMoves) <= 0 or roundNum >= maxRounds :
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

    for move in  validMoves:
      boardClone = board.get_clone()
      boardClone.play(move, self.color)
      movTempValue = self.getMovementValue(self.color, boardClone, 1, 1, 2)
      if movValue == None or movValue < movTempValue:
        myMove = move
        movValue = movTempValue

    return myMove