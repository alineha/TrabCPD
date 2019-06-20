from hash import *

class HashUserNode:

	def __init__(self, userID, ratings):

		self.userID = userID

		#LISTA de listas no formato [movieID, rating]
		self.ratings = ratings


	def __str__(self):
		return "USER ID: {} | MOVIE RATINGS {} ".format(self.userID, self.ratings)



class HashUser:

	def __init__(self, size = 20000):

		self.size = size

		self.table = [None]*size

		self.taken = 0
		

	def insert(self, userID, movieID, rating):
		
		t = 0
		code = userID % self.size

		while self.table[code] != None:
			if userID == self.table[code].userID:
				self.nodeUpdt(code, movieID, rating)
				return
			else: code, t = self.colision(code, t)

		aux = [[movieID, rating]]
		self.table[code] = HashUserNode(userID, aux)
		self.taken += 1
		del aux

	def colision(self, code, t):

		t = t + 1
		code = int(code + 0.5*t + 0.5*t*t) % self.size
		return code, t

	def nodeUpdt(self, code, movieID, rating):
		self.table[code].ratings.append([movieID, rating])


	def printHash(self):
		print(self)
		for nodo in self.table:
			print(str(nodo))


	def __str__(self):
		return " * SIZE: {} | TAKEN: {} | RATE: {}".format(self.size, self.taken, (self.taken/self.size)*100)
