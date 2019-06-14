from hash import *
from trie import *
import csv

def openF():

	hashMovie = HashMovie()
	hashUser = HashUser()
	trie = Trie()

	fmovie = open('movie.csv', 'r', encoding="utf8")
	csv_fmovie = csv.reader(fmovie)
	next(csv_fmovie)
	for line in csv_fmovie:
		movieID = int(line[0])
		title = line[1]
		if line[2] != "(no genres listed)":
			genres = line[2].split("|")
		else:genres = []
		trie.insert(title,movieID)
		hashMovie.insert(movieID, title, genres, None)
	
	frat =  open('minirating.csv', 'r', encoding="utf8") 
	next(frat)

	for line in frat:
		line = line.split(",")
		userID = int(line[0])
		movieID = int(line[1])
		rating = float(line[2])
		hashMovie.insert(movieID, None, None, rating)
		hashUser.insert(userID, movieID, rating)

	frat.close()
	fmovie.close()

	hashUser.printHash()
		
	

def main():

	openF()



if __name__ == "__main__":
	main()
