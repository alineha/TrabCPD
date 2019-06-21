from hash import *

class HashMovieNode:

	def __init__(self, movieID, title, genres = None, meanRat = None):

		self.movieID = movieID

		self.title = title
	
		self.genres = genres
		
		self.meanRat = meanRat
		
		self.count = 0

	def __str__(self):
		return "TITLE: {} | MOVIE ID: {} | MEAN RATING: {} | COUNT: {}".format(self.title, self.movieID, self.meanRat, self.count) + " | GENRES: " +  str(self.genres)

class HashMovie:

	def __init__(self, size):

		self.size = size

		self.table = [None]*size

		self.taken = 0


	def insert(self, movieID, title, genres, rating):
		
		t = 0
		code = movieID % self.size

		while self.table[code] != None:

			if movieID == self.table[code].movieID:

				self.table[code] = self.nodeUpdt(self.table[code], rating)
				return 
				
			else: code, t = self.colision(code, t)

		self.table[code] = HashMovieNode(movieID, title, genres, rating)
		self.taken += 1

	def colision(self, code, t):

		t = t + 1
		code = int(code + 0.5*t + 0.5*t*t) % self.size
		return code, t


	def nodeUpdt(self, node, rating):
	
		if node.meanRat == None:
			node.meanRat = rating

		else: 
			node.meanRat = (rating + node.meanRat*self.taken)/(self.taken+1)
		
		node.count += 1
		return node


	def printHash(self):
		print(self)
		'''
		for nodo in self.table:
			print(str(nodo))

		'''


	def __str__(self):
		return " * SIZE: {} | TAKEN: {} | RATE: {}".format(self.size, self.taken, (self.taken/self.size)*100)