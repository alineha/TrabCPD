#coding=UTF-8

class HashMovieNode:

	def __init__(self, movieID, title = None, genres = None, meanRat = None):

		self.movieID = movieID

		self.title = title
	
		self.genres = genres
		
		self.meanRat = meanRat
		
		self.count = 0

	def __str__(self):
		return "TITLE: {} | MOVIE ID: {} | MEAN RATING: {} | COUNT: {}".format(self.title, self.movieID, self.meanRat, self.count) + " | GENRES: " +  str(self.genres)

class HashMovie:

	def __init__(self, size = 28000):

		self.size = size

		self.table = [None]*size

		self.taken = 0

		self.rate = (self.taken / self.size)*100
		

	def insert(self, movieID, title, genres, rating):
		
		t = 0
		code = movieID % self.size
		while self.table[code] != None:
			if movieID == self.table[code].movieID:
				self.nodeUpdt(code, rating)
				return
			else: code, t = self.colision(code, t)

		self.table[code] = HashMovieNode(movieID, title, genres, rating)
		self.incTaken()
		self.reSize()
			

	def colision(self, code, t):

		t = t + 1
		code = int(code + 0.5*t + 0.5*t*t) % self.size
		return code, t

	def search(self, movieID):

		t = 0
		code = movieID % self.size
		while self.table[code] != None:
			if movieID == self.table[code].movieID:
				return self.table[code]
			else: code, t = self.colision(code, t)
		return None



	def nodeUpdt(self, code, rating):
	
		if self.table[code].meanRat == None:
			self.table[code].meanRat = rating
		else: self.table[code].meanRat = (rating + self.table[code].meanRat)/2
		
		self.table[code].count += 1


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



class HashUserNode:

	def __init__(self, userID, userRat):

		self.userID = userID

		#LISTA de dicionarios com {movieID: rating}
		self.userRat = userRat


	def __str__(self):
		return "USER ID: {} | MOVIE RATINGS {} ".format(self.userID, self.userRat)



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

		c = 0.5
		t = t + 1
		code = int(code + c*t + c*t*t) % self.size
		return code, t

	def search(self, userID):

		t = 0
		code = userID % self.size
		while self.table[code] != None:
			if userID == self.table[code].userID:
				print("AAAAAAAAA")
				return self.table[code]
			else: code, t = self.colision(code, t)
		return None


	def nodeUpdt(self, code, movieID, rating):
	
		self.table[code].userRat[movieID] = rating


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
