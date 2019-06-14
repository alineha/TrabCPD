#coding=UTF-8

#Nodo da estrutura hash
class nodeHashT:

	def __init__(self, title, movieID, genres, meanRat):

		self.title = title

		self.movieID = movieID
	
		self.genres = genres
		
		self.meanRat = meanRat
		
		self.count = 0

	def __str__(self):
		return "TITLE: {} | MOVIE ID: {} | MEAN RATING: {} | COUNT: {}".format(self.title, self.movieID, self.meanRat, self.count) + " | GENRES: " +  str(self.genres)

class HashT:

	def __init__(self, size = 64):

		self.size = size

		self.table = [None]*size

		self.taken = 0

		self.rate = (self.taken / self.size)*100
		

	def insert(self, title, movieID, genres, rating):
		
		t = 0
		code = movieID % self.size
		while self.full(code):
			if movieID == self.table[code].movieID:
				self.nodeUpdt(code, rating)
				return
			else: 
				code, t = self.colision(code, t)

		node = nodeHashT(title, movieID, genres, rating)
		self.table[code] = node
		self.incTaken()
		self.reSize()
		del node


	def full(self, code):

		return False if self.table[code] == None else True
			

	def colision(self, code, t):

		c = 0.5
		t = t + 1
		code = int(code + c*t + c*t*t) % self.size
		return code, t


	def nodeUpdt(self, code, rating):
	
		#self.table[code].genres = genres
		if self.table[code].meanRat == None:
			self.table[code].meanRat = rating
		else:
			self.table[code].meanRat = (rating + self.table[code].meanRat)/2
		
		self.table[code].count += 1


	def reSize(self):

		if self.rate >= 66:
			listAux = [None]*self.size 
			self.table.extend(listAux) 
			del listAux
			self.size = len(self.table)
			self.rate = (self.taken/self.size)*100

	def incTaken(self):
		self.taken = self.taken + 1
		self.rate = (self.taken/self.size)*100


	def printHashT(self):
		print(self)
		for nodo in self.table:
			print(str(nodo))


	def __str__(self):
		return " * SIZE: {} | TAKEN: {} | RATE: {}".format(self.size, self.taken, self.rate)
