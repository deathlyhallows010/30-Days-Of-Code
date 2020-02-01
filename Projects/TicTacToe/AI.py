import random

class AI:

	def pickSpot(self, game):
		choices = []
		for i in range(len(game.board)):
			if game.board[i] == '-':
				choices.append(i+1)

		return random.choice(choices)