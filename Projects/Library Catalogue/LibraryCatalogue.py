import math
import random

from Book import Book

class LiberaryCatalogue:

	## Properties, Fields, Global Variables
	bookCollection = {}
	currentDay = 0
	lengthOfCheckOut = 15
	initialFees = 10
	feePerLateDay = 2

	def __init__(self, collection):
		self.bookCollection = collection

	## Gatters
	def getCurrentDay(self):
		return self.currentDay

	def getBookCollection(self):
		return self.bookCollection

	def getBook(self,bookTitle):
		return self.bookCollection[bookTitle]

	def getLenghtofBookCheckoutPeriod(self):
		return self.lengthOfCheckOut

	def getInitialLateFees(self):
		return self.initialFees

	def getFeeperday(self):
		return self.feePerLateDay

	## Setters

	def nextDay(self):
		self.currentDay += 1

	def SetDay(self, day):
		self.currentDay = day

	## Instance Method

	def CheckoutBook(self,title):
		book = self.getBook(title)
		if book.getIsCheckedOut():
			self.sorryBookAlreadyCheckedOut(book)
		else:
			book.SetIsCheckedOut(True, self.currentDay)
			print("You checked out " + title + " successfully"
				", Its Due on Date " + str(self.getCurrentDay() + self.getLenghtofBookCheckoutPeriod()) + ".")

	def ReturnBook(self, title):
		book =  self.getBook(title)
		daysLate = self.currentDay - (book.getDayCheckedOut() + 
		self.getLenghtofBookCheckoutPeriod())
		if daysLate > 0:
			print("You owe the liberary Rs." +
			 str(self.getInitialLateFees()+ daysLate*self.getFeeperday())+
			" because your book is " + str(daysLate) + " days overdue.")
		else:
			print("Book Returned. Thank You")
		book.SetIsCheckedOut(False, -1)

	def sorryBookAlreadyCheckedOut(self,book):
		print("Sorry, " + book.getTitle() + " is already checked out."+
			" It is expected to return on day " + str(book.getDayCheckedOut()+ 
				self.getLenghtofBookCheckoutPeriod()) + ".")



if __name__ == '__main__':

	bookCollection = {}
	book1 = Book("Harry Potter", 827132, 9999999)
	book2 = Book("Game of Thrones", 875624, 8876956)
	book3 = Book("Telford", 557558, 585589)
	book4 = Book("Keary", 85686,54848)
	book5 = Book("Gildart", 745412,365854)

	bookCollection["Harry Potter"] = book1
	bookCollection["Game of Thrones"] = book2
	bookCollection["Telford"] = book3
	bookCollection["Keary"] = book4
	bookCollection["Gildart"] = book5

	print(bookCollection)
	print("********************************************************************")

	lib = LiberaryCatalogue(bookCollection)
	lib.CheckoutBook("Harry Potter")
	lib.nextDay()
	lib.nextDay()
	lib.CheckoutBook("Harry Potter")
	lib.SetDay(17)
	lib.ReturnBook("Harry Potter")
	lib.CheckoutBook("Harry Potter")
	lib.ReturnBook("Harry Potter")
	lib.CheckoutBook("Gildart")
	lib.ReturnBook("Gildart")
	
	print("********************************************************************")



	