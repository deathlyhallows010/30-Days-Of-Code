from TicTacToe import TicTacToe
from AI import AI

class TicTacToeApplication:

	def play(self):
		
		doYouWantToPlay = True

		while(doYouWantToPlay):
			print("Welcome to Tic Tac Toe!\n"
				+ "Pick your character")
			playerToken = input()
			print("Pick Oppenent character")
			opponentToken = input()

			game = TicTacToe(playerToken, opponentToken)
			ai = AI()

			print('\n Enter a number from 1-9\n')
			game.printIndexBoard()


			while(game.gameOver() == 'notOver'):
				if game.currentMarker == game.userMarker:
					# User's Turn
					print("Please enter the spot from token")
					spot = int(input())
					while (not game.playTurn(spot)):
						print("Invalid Choice")
						spot = int(input())
					print("You picked "+ str(spot) + "!")
				else:
					# AI Turn
					aiSpot = ai.pickSpot(game)
					game.playTurn(aiSpot)
					print("AI picked "+ str(aiSpot) + "!")

				print()
				game.printBoard()

			print(game.gameOver())
			print("\n To Play Again enter 'Y' or press any other key")
			response = input()
			doYouWantToPlay =  (response == 'Y')
			print()

if __name__ == "__main__":
	obj = TicTacToeApplication()
	obj.play()
						
			

			
