
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

	lista = []

	nodeGenre = searchStr(hashGenre, genre)

	for movieID in nodeGenre.movies:
		nodeMovie = search(hashMovie, movieID)

		if nodeMovie.count > 10:
			lista.append(nodeMovie)

	i = 0
	print("\n--- TOP "+ top +" "+ genre.upper() + " ---\n")
	
	for i in range(top):
		print(lista[i])
 

	
def searchTags(hashGenre, word):

	info = ["Brazil", "drugs"]

	beg = 0
	end = len(info)
	
	tags = [ info[info.find("'", beg, end) : info.find("'", info.find("'", beg, end), end)] ]
	
	while beg != end:
		beg = info.find("'", beg, end)
		tags.append(info[beg : info.find("'", beg, end)])

	node = []

	for tag in tags:
		node.append(searchStr(hashGenre, genre))
	
	#tem que arranjar um jeito de fazer a intersecção das listas desses nodos
 