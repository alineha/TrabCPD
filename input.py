from hashFunctions import *
from trie import *
import csv

def openF():

	trie = Trie()
	hashMovie = HashMovie(size = 45000)
	hashUser = HashUser(size = 250000)
	hashGenre = HashString(size = 50)
	hashTag = HashString(size = 65000)
	

	fmovie = open('movie.csv', 'r', encoding="utf8")
	csv_fmovie = csv.reader(fmovie)
	next(csv_fmovie)

	for line in csv_fmovie:

		movieID = int(line[0])
		title = line[1]

		if line[2] != "(no genres listed)":
			genres = line[2].split("|")

			for genre in genres:
				hashGenre.insert(genre, movieID)

		else: genres = None

		trie.insert(title.lower(), movieID)
		hashMovie.insert(movieID, title, genres, None)

	fmovie.close()

	frat =  open('ratingOpt.csv', 'r', encoding="utf8") 
	next(frat)

	for line in frat:
		
		line = line.split(",")
		userID = int(line[0])
		movieID = int(line[1])
		rating = float(line[2])

		hashMovie.insert(movieID, None, None, rating)
		hashUser.insert(userID, movieID, rating)

	frat.close()

	ftag = open('tagOpt.csv', 'r', encoding='utf8')
	csv_ftag = csv.reader(ftag)
	next(csv_ftag)

	for line in csv_ftag:
		movieID = int(line[1])
		tag = (line[2]).lower()
		hashTag.insert(tag, movieID)

	ftag.close()


	return trie, hashMovie, hashUser, hashGenre, hashTag

		
