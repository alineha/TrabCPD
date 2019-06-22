from listFunctions import *
from hashFunctions import *


def searchTitle(trie, hashMovie, prefix):

	lista = []

	for movieID in trie.search(prefix):
		lista.append(search(hashMovie, movieID))

	print("\n** per total ratings count **\n")
	for movie in mergesort(lista, "count"):
		print(movie)


def searchUser(hashUser, hashMovie, userID):

	user = search(hashUser, userID)
	if user == None:
		return print("User not found!")
	else:
		for sublist in user.ratings:
			node = search(hashMovie, sublist[0])
			print("USER "+ str(userID) + " | RATING: " + str(sublist[1]) +" | " + str(node))


def searchGenre(hashGenre, hashMovie, top, genre):

	i = 0
	lista = []

	nodeGenre = searchStr(hashGenre, genre)

	for movieID in nodeGenre.movies:
		nodeMovie = search(hashMovie, movieID)

		if nodeMovie.count > 1000:
			lista.append(nodeMovie)


	print("\n--- TOP "+ str(top) +" "+ genre.upper() + " ---\n")

	for movie in mergesort(lista, "meanRat"):
		print(movie)
		i += 1
		if i >= top: break

	
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

	print("\n** per total ratings count **\n")
	for movie in mergesort(listaSec, "count"): print(movie)

	
 

