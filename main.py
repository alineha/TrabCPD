# coding=UTF-8
from hash import *
from trie import *
from input import *

def searchTitle(trie, hashMovie):

	prefix = "Star Wars"#input("Insira nome ou prefixo do filme: ")
	#while prefix != 'quit':
	for MovieID in trie.search(prefix):
		print(search(hashMovie, MovieID))
		#prefix = input("\nInsira nome ou prefixo do filme: ")

def searchUser(hashMovie, hashUser):

	#info = input("Insira ID do usuario: ")
	user = search(hashUser,48644)

	#while info != 'quit':
	for lista in user.ratings:
		node = search(hashMovie, lista[0])
		print(str(node) + " | USER "+ str(48644) + " RATING: " + str(lista[1]))
	#info = input("\nInsira ID de usuario: ")

def searchGenre(hashGenre):

	info = "top10 Fantasy"#input("Insira nome ou prefixo do filme: ")
	#while info != 'quit':
	top = info[3 : info.find(" ")]
	genre = info[info.find(" ") + 1 :]
	
	node = searchStr(hashGenre, genre)

	i = 0
	print("\n--- TOP "+ top +" "+ genre.upper() + " ---\n")
	for movie in node.movies:
		print(movie)
		i += 1
		if i >= int(top): break 

def searchTags(hashGenre):

	info = "'Brazil' 'drugs'"

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

def main():

	trie, hashMovie, hashUser, hashGenre, hashTag = openF()

	#hashMovie.printHash()
	#hashUser.printHash()
	#hashGenre.printHash()
	#searchTitle(trie, hashMovie)
	#searchUser(hashMovie, hashUser)
	#searchGenre(hashGenre)
	#searchTags(hashTags)

if __name__ == "__main__":
    main()
