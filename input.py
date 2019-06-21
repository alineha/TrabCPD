from hash import *
from trie import *
import csv

#provisório, enquanto n temos função de sort
def takeRatings(elem):
    return elem.meanRat

def openF():

	trie = Trie()
	hashMovie = HashMovie(size = 60000)
	hashUser = HashUser(size = 30000000)
	hashGenre = HashString(size = 100)
	hashTag = HashString(size = 70000)

	fmovie = open('movie.csv', 'r', encoding="utf8")
	csv_fmovie = csv.reader(fmovie)
	next(csv_fmovie)

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

	fmovie.close()

	frat =  open('rating.csv', 'r', encoding="utf8") 
	next(frat)

	#i=0
	for line in frat:
		#print(i)
		#i+=1
		line = line.split(",")
		userID = int(line[0])
		movieID = int(line[1])
		rating = float(line[2])
		#atualiza ratings na hash de movies
		hashMovie.insert(movieID, None, None, rating)
		#preenche hash de users
		hashUser.insert(userID, movieID, rating)

	frat.close()

	# para cada filme na hash movie ve todos os generos da sua lista e copia esse filme 
	# (o nodo inteiro, não só o ID e rating) para lista do genero correspondente do hash genre
	for movie in hashMovie.table:
		if movie != None and movie.genres != None and movie.count > 10:
			for genre in movie.genres:
				hashGenre.insert(genre, movie)

	#ordena a lista do genero na hash genre por ratings
	#for node in hashGenre.table:
	#	if node != None:
	#		node.movies.sort(key=takeRatings, reverse=True)


	ftag = open('tag.csv', 'r', encoding='utf8')
	csv_ftag = csv.reader(ftag)
	next(csv_ftag)

	for line in csv_ftag:
		movieID = line[1]
		tag = line[2]
		hashTag.insert(tag, movieID)

	ftag.close()

	return trie, hashMovie, hashUser, hashGenre, hashTag

		
