# coding=UTF-8
from hash import *
from trie import *
from input import *

def searchTitle(trie, hashMovie):

	prefix = input("Insira nome ou prefixo do filme: ")
	while prefix != 'quit':
		for MovieID in trie.search(prefix):
			print(hashMovie.search(MovieID))
		prefix = input("\nInsira nome ou prefixo do filme: ")

def searchUser(hashMovie, hashUser):

	#userID = input("Insira ID do usuario: ")
	user = hashUser.search(48644)
	print(user)

	#while userID != 'quit':
	for MovieID,rating in user.userRat.items():
		node = hashMovie.search(MovieID)
		print(node.title,MovieID,rating)
	prefix = input("\nInsira nome ou prefixo do filme: ")


def main():
	
	trie, hashMovie, hashUser = openF()
	# searchTitle(trie, hashMovie)
	searchUser(hashMovie,hashUser)




if __name__ == "__main__":
    main()
