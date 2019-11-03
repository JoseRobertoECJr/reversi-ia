from models.move import Move
from anytree import Node, RenderTree, NodeMixin

MAX_ROUNDS = 2
EMPTY, BLACK, WHITE, OUTER = '.', '@', 'o', '?'


class Round(NodeMixin):
  def __init__(self, player, parent, isMyTurn):
    self.board = Board(None)
    self.player = player

  def getMovement():

    validMovesLength = len(self.board.valid_moves(self.color))
    if validMovesLength <= 0:
      return self.getMinMaxValue()

  def getMinMaxValue():
    score = self.board.score()
    if self.player.color == WHITE:
      return score[0] - score[1]
    else:
      return score[1] - score[0]

class HumanPlayer:
  
  def __init__(self, color):
    self.color = color


  def play(self, board):
  
    rowInp = int(raw_input("Linha: "))
    colInp = int(raw_input("Coluna: "))
    move = Move(rowInp, colInp)

    prof = 0
    while prof < self.prof
      board.valid_moves(self.color)
      self.board.play(self.atual_player.play(self.board.get_clone()), atual_color)
      prof++

    while move not in board.valid_moves(self.color):
      move = Move(rowInp, colInp)
	  
    return move
