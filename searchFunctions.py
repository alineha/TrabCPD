from listFunctions import *
from hashFunctions import *


def searchTitle(trie, hashMovie, prefix):

	for movieID in trie.search(prefix):
		print(search(hashMovie, movieID))

def searchUser(hashUser, hashMovie, userID):

	for sublist in user.ratings:
		node = search(hashMovie, sublist[0])
		print(str(node) + " | USER "+ str(userID) + " RATING: " + str(sublist[1]))

def searchGenre(hashGenre, hashMovie, top, genre):

	'''
	top = info[3 : info.find(" ")]
	genre = info[info.find(" ") + 1 :]
	'''
	i = 0
	lista = []

	nodeGenre = searchStr(hashGenre, genre)

	for movieID in nodeGenre.movies:
		nodeMovie = search(hashMovie, movieID)

		if nodeMovie.count > 10:
			lista.append(nodeMovie)


	print("\n--- TOP "+ str(top) +" "+ genre.upper() + " ---\n")

	for movie in mergesort(lista, True, True):
		print(movie)
		if i >= top: break
 

	
def searchTags(hashTag, hashMovie):

	#tags = ["cute", "emotional","romantic"]

	lista = []

	for tag in tags:

		nodeTag = searchStr(hashTag, tag)
		
		if nodeTag == None:
			return print("Filmes não encontrados!")

		elif not lista:
			[lista.append(movie) for movie in nodeTag.movies if movie not in lista]

		else: 
			for movie in lista:
				if movie not in nodeTag.movies:
					lista.remove(movie)

	
	for ID in mergesort(lista):
		print(search(hashMovie,ID))
	
 

