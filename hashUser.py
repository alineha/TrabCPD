from hash import *

class HashUserNode:

	def __init__(self, userID, ratings):

		self.userID = userID

		#LISTA de dicionarios com {movieID: rating}
		self.ratings = ratings


	def __str__(self):
		return "USER ID: {} | MOVIE RATINGS {} ".format(self.userID, self.ratings)



class HashUser:

	def __init__(self, size = 28000):

		self.size = size

		self.table = [None]*size

		self.taken = 0

		self.rate = (self.taken / self.size)*100
		

	def insert(self, userID, movieID, rating):
		
		t = 0
		code = userID % self.size

		while self.table[code] != None:
			if userID == self.table[code].userID:
				self.nodeUpdt(code, movieID, rating)
				return
			else: code, t = self.colision(code, t)

		auxRat = {}
		auxRat[movieID] = rating 
		self.table[code] = HashUserNode(userID, auxRat)
		self.incTaken()
		self.reSize()
		del auxRat

	def colision(self, code, t):

		t = t + 1
		code = int(code + 0.5*t + 0.5*t*t) % self.size
		return code, t

	def nodeUpdt(self, code, movieID, rating):
	
		self.table[code].ratings[movieID] = rating


	def reSize(self):

		if self.rate >= 67:
			listAux = [None]*self.size 
			self.table.extend(listAux) 
			del listAux
			self.size = len(self.table)
			self.rate = (self.taken/self.size)*100


	def incTaken(self):
		self.taken = self.taken + 1
		self.rate = (self.taken/self.size)*100


	def printHash(self):
		print(self)
		for nodo in self.table:
			print(str(nodo))


	def __str__(self):
		return " * SIZE: {} | TAKEN: {} | RATE: {}".format(self.size, self.taken, self.rate)
