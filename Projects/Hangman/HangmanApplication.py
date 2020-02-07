from Hangman import Hangman

class HangmanApplication:

	def play(self):

		print("I will pick a word and you will "
                + "try to guess it character "
                + "by character.\n")

		doYouEantToPlay = True

		while(doYouEantToPlay):
			game = Hangman

			while (not game.gameOver):
				print(game.drawPicture())
				print()
				print(game.getFormalCurrentGuess())

				print(game.mysteryWord)
				print()

				print("Enter the Character\n")
				guess = input()
				print()

				while (game.isGuessedAlready(guess)):
					print("Word already guessed\n")
					guess = input()

				if game.playGuess(guess):
					print('Great guess!\n')
				else:
					print("Unfortunately that's not the character")

			print("\n Press 'Y' to play the game again")
			response = input()
			doYouEantToPlay = (response == 'Y')
			print()


                