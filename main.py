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
	for movieID, rating in user.ratings.items():
		node = search(hashMovie, movieID)
		print(str(node) + " | USER "+ str(48644) + " RATING: " + str(rating))
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
		
		
def main():
	
	trie, hashMovie, hashUser, hashGenre = openF()

	#hashMovie.printHash()
	#hashUser.printHash()
	#hashGenre.printHash()
	#searchTitle(trie, hashMovie)
	#searchUser(hashMovie, hashUser)
	#searchGenre(hashGenre)


if __name__ == "__main__":
    main()
