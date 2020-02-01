class TicTacToe:

	def __init__(self, playerToken, aiMarker):
		self.userMarker = playerToken
		self.aiMarker = aiMarker
		self.winner = '-'
		self.board = self.setBoard()
		self.currentMarker = playerToken

	def setBoard(self):
		return ['-']*9

	def playTurn(self, spot):
		isValid = self.withinRange(spot) and ( not self.isSpotTaken(spot))
		if isValid:
			self.board[spot-1] = self.currentMarker
			if self.currentMarker == self.userMarker:
				self.currentMarker = self.aiMarker
			else:
				self.currentMarker = self.userMarker
		return isValid

	def withinRange(self, number):
		return number>0 and number<(len(self.board) +1) 

	def isSpotTaken(self, number):
		return self.board[number-1] != '-'

	def printBoard(self):
		
		for i in range(len(self.board)):
			if i%3 == 0 and i != 0:
				print("\n  ------------")
			print(" | " + self.board[i] ,end = ' ')
		print()
		print()
		

	def printIndexBoard(self):
		
		for i in range(len(self.board)):
			if i%3 == 0 and i != 0:
				print("\n  ------------")
			print(" | " + str(i+1), end = ' ')
		print()
		print()

	def isThereAWinner(self):
		diagonalsAndMiddles = (self.rightDi() or self.leftDi() or self.middleRow() or self.secondCol()) and self.board[4] != '-'
		topAndFirst = (self.topRow() or self.firstCol()) and self.board[0] != '-'
		bottomAndThird = (self.bottomRow() or self.thirdCol()) and self.board[8] != '-'
		if (diagonalsAndMiddles):
			self.winner = self.board[4]
		elif (topAndFirst):
			self.winner = self.board[0]
		elif (bottomAndThird):
			self.winner = self.board[8]
        
		return diagonalsAndMiddles or topAndFirst or bottomAndThird

	def topRow(self):
		return (self.board[0] == self.board[1]) and (self.board[1] == self.board[2])

	def middleRow(self):
		return (self.board[3] == self.board[4]) and (self.board[4] == self.board[5])

	def bottomRow(self):
		return (self.board[6] == self.board[7]) and (self.board[7] == self.board[8])

	def firstCol(self):
		return (self.board[0] == self.board[3]) and (self.board[3] == self.board[6])
	
	def secondCol(self):
		return (self.board[1] == self.board[4]) and (self.board[4] == self.board[7])

	def thirdCol(self):
		return (self.board[2] == self.board[5]) and (self.board[5] == self.board[8])

	def rightDi(self):
		return (self.board[0] == self.board[4]) and (self.board[4] == self.board[8])

	def leftDi(self):
		return (self.board[2] == self.board[4]) and (self.board[4] == self.board[8])

	def istheBoardFilled(self):
		if '-' in self.board:
			return False
		return True

	def gameOver(self):
		if self.isThereAWinner():
			return 'The winner is ' + self.winner
		elif self.istheBoardFilled():
			return 'Draw: Game Over!!!'
		else:
			return 'notOver'





