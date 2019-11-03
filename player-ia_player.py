from models.move import Move
from anytree import Node, RenderTree, NodeMixin

MAX_ROUNDS = 2
ROUNDS = 1
EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'


class Round(NodeMixin):
  def __init__(self, color, board, parent=None):
    self.board = board
    self.color = color

  def getMovementValue(self, isMyTurn):

    validMoves = self.board.valid_moves(self.color)

    if len(validMoves) <= 0 or ROUNDS >= MAX_ROUNDS :
      return isMyTurn * self.getMinMaxValue()
    else:
      movValue = None
      
      for move in  validMoves:
        movTempValue = Round(self.color, self.board.get_clone().play(move), self).getMovementValue(isMyTurn)
        if movValue == None or (isMyTurn * movValue < isMyTurn * movTempValue):
          movValue = movTempValue

      return movValue

  def getMinMaxValue(self):
    score = self.board.score()
    if self.color == WHITE:
      return score[0] - score[1]
    else:
      return score[1] - score[0]



class HumanPlayer:
  
  def __init__(self, color):
    self.color = color

  def play(self, board):
  
    move = self.getMovement(board)
	  
    return move

  def getMovement(self, board):

    validMoves = board.valid_moves(self.color)
    movValue = None
    myMove = None

    for move in  validMoves:
      movTempValue = Round(self.color, board.get_clone().play(move)).getMovementValue(1)
      if movValue == None or movValue < movTempValue:
        myMove = move
        movValue = movTempValue

    return myMove
