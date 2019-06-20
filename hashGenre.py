from hash import *
from hashMovie import *

class HashGenreNode:

	def __init__(self, genre):
	
		self.genre = genre

		self.movies = []


	def __str__(self):
		return "GENRE: {} | ".format(self.genre)

class HashGenre:

	def __init__(self, size = 50):

		self.size = size

		self.table = [None]*size

		self.taken = 0


	def insert(self, genre, movie):
		
		t = 0
		code = 0

		for ch in genre:
			code = (code*33 + ord(ch)) % self.size

		while self.table[code] != None:

			if genre == self.table[code].genre:
				self.nodeUpdt(code, movie)
				return
			else: 
				code, t = self.colision(code, t)

		self.table[code] = HashGenreNode(genre)
		self.nodeUpdt(code, movie)
		self.taken += 1


	def colision(self, code, t):

		t = t + 1
		code = int(code + 0.5*t + 0.5*t*t) % self.size
		return code, t


	def nodeUpdt(self, code, movie):
	
		self.table[code].movies.append(movie)


	def printHash(self):
		print(self)
		for nodo in self.table:
			if nodo != None:
				print("\n----- GENRE: " + nodo.genre + " -----\n")
				for movie in nodo.movies:
					print(str(movie))


	def __str__(self):
		return " * SIZE: {} | TAKEN: {} | RATE: {}".format(self.size, self.taken, (self.taken/self.size)*100)