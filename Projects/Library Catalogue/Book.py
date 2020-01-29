class Book:

	## Properties, Fields, Global Variables
	title = None
	pageCount = None
	ISBN = None
	isCheckOut = False
	dayCheckedOut  = - 1

	## Constructor
	def __init__(self, Booktitle, bookpagecont, bookISBN):
		self.title = Booktitle
		self.pageCount = bookpagecont
		self.ISBN = bookISBN

	## Getters --> INSTANCE METHODS
	def getTitle(self):
		return self.title

	def getPageCount(self):
		return self.pageCount

	def getISBN(self):
		return self.ISBN

	def getIsCheckedOut(self):
		return self.isCheckOut

	def getDayCheckedOut(self):
		return self.dayCheckedOut

	## Setters
	def SetIsCheckedOut(self,newIsCheckedOut, curretDayCheckOut):
		self.isCheckOut = newIsCheckedOut
		self.__setDayCheckedOut(curretDayCheckOut)

	def __setDayCheckedOut(self,day):
		self.dayCheckedOut = day
