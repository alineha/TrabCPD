from listFunctions import *
from hashFunctions import *


def searchTitle(trie, hashMovie, prefix):

	lista = []

	for movieID in trie.search(prefix):
		lista.append(search(hashMovie, movieID))

	return mergesort(lista, "count")


def searchUser(hashUser, hashMovie, userID):

	lista = []
	user = search(hashUser, userID)
	if user == None:
		return print("User not found!")
	else:
		for sublist in user.ratings:
			node = search(hashMovie, sublist[0])
			lista.append([str(userID), str(sublist[1]), node])
	return lista


def searchGenre(hashGenre, hashMovie, top, genre):

	i = 0
	lista = []

	nodeGenre = searchStr(hashGenre, genre)

	for movieID in nodeGenre.movies:
		nodeMovie = search(hashMovie, movieID)

		if nodeMovie.count > 1000:
			lista.append(nodeMovie)


	return mergesort(lista, "meanRat")[:top]

	
def searchTags(tags, hashTag, hashMovie):

	lista = []

	for tag in tags:

		nodeTag = searchStr(hashTag, tag)
		
		if nodeTag == None:
			return print("Filmes não encontrados!")

		else:

			listaSec = nodeTag.movies

			if not lista:
				[lista.append(movie) for movie in nodeTag.movies if movie not in lista]

			else: 
				for movie in lista:
					if movie not in listaSec: lista.remove(movie)

	listaSec.clear()

	for ID in lista:
		listaSec.append(search(hashMovie, ID))

	return mergesort(listaSec, "count")

	
 

