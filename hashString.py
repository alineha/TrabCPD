from hash import *
from hashMovie import *

class HashStringNode:

	def __init__(self, string):
	
		self.string = string

		self.movies = []


	def __str__(self):
		return "STRING: {} | ".format(self.string)

class HashString:

	def __init__(self, size):

		self.size = size

		self.table = [None]*size

		self.taken = 0


	def insert(self, string, movie):
		
		t = 0
		code = 0

		for ch in string:
			code = (code*33 + ord(ch)) % self.size

		while self.table[code] != None:

			if string == self.table[code].string:
				self.nodeUpdt(code, movie)
				return
			else: 
				code, t = self.colision(code, t)

		self.table[code] = HashStringNode(string)
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
				print("\n----- STRING: " + nodo.string + " -----\n")
				for movie in nodo.movies:
					print(str(movie))


	def __str__(self):
		return " * SIZE: {} | TAKEN: {} | RATE: {}".format(self.size, self.taken, (self.taken/self.size)*100)
