from hash import *
from trie import *
import csv

#provisório, enquanto n temos função de sort
def takeRatings(elem):
    return elem.meanRat

def openF():

	trie = Trie()
	hashMovie = HashMovie()
	hashUser = HashUser()
	hashGenre = HashGenre()

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

		#a trie é completa com um arquivo, a hash de movie não
		trie.insert(title,movieID)
		#temos que preencher as ratings em outro arquivo 
		hashMovie.insert(movieID, title, genres, None)
	

	for line in frat:

		line = line.split(",")
		userID = int(line[0])
		movieID = int(line[1])
		rating = float(line[2])
		#atualiza ratings na hash de movies
		hashMovie.insert(movieID, None, None, rating)
		#preenche hash de users
		hashUser.insert(userID, movieID, rating)

	frat.close()
	fmovie.close()

	# para cada filme na hash movie ve todos os generos da sua lista e copia esse filme 
	# (o nodo inteiro, não só o ID e rating) para lista do genero correspondente do hash genre
	for movie in hashMovie.table:
		if movie != None and movie.genres != None and movie.count > 10:
			for genre in movie.genres:
				hashGenre.insert(genre, movie)

	#ordena a lista do genero na hash genre por ratings
	for node in hashGenre.table:
		if node != None:
			node.movies.sort(key=takeRatings, reverse=True)


	return trie, hashMovie, hashUser, hashGenre

		
