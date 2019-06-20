from hash import *
from trie import *
import csv

def takeRatings(elem):
    return elem.meanRat

def openF():

	hashMovie = HashMovie()
	hashUser = HashUser()
	hashGenre = HashGenre()
	trie = Trie()

	frat =  open('minirating.csv', 'r', encoding="utf8") 
	fmovie = open('movie.csv', 'r', encoding="utf8")
	csv_fmovie = csv.reader(fmovie)
	next(csv_fmovie)
	next(frat)

	for line in csv_fmovie:

		movieID = int(line[0])
		title = line[1]

		if line[2] != "(no genres listed)":
			genres = line[2].split("|")
		else: genres = None

		trie.insert(title,movieID)
		hashMovie.insert(movieID, title, genres, None)
	

	for line in frat:

		line = line.split(",")
		userID = int(line[0])
		movieID = int(line[1])
		rating = float(line[2])
		hashMovie.insert(movieID, None, None, rating)
		hashUser.insert(userID, movieID, rating)

	frat.close()
	fmovie.close()

	for movie in hashMovie.table:
		if movie != None and movie.genres != None and movie.count > 10:
			for genre in movie.genres:
				hashGenre.insert(genre, movie)

	for node in hashGenre.table:
		if node != None:
			node.movies.sort(key=takeRatings, reverse=True)


	return trie, hashMovie, hashUser, hashGenre

		
