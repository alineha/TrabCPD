# coding=UTF-8
from hashFunctions import *
from trie import *
from input import *
import time
from console import *

def main():

	t0 = time.time()

	trie, hashMovie, hashUser, hashGenre, hashTag = openF()

	t1 = time.time()
	total = t1-t0
	print("\nFinished Loading. Time:",total)

	console(trie, hashMovie, hashUser, hashGenre, hashTag)
	
	'''
	print("\n**********MOVIE**********")
	hashMovie.printHash()
	print("**********USER***********")
	hashUser.printHash()
	print("**********GENRE**********")
	hashGenre.printHash()
	
	print("**********TAGS**********")
	hashTag.printHash()
	searchTitle(trie, hashMovie)
	searchUser(hashMovie, hashUser)
	'''
	#searchGenre(hashGenre, hashMovie, 10, "Horror")
	#searchTags(hashTag, hashMovie)
	#print("**********TAGS**********")
	#hashTag.printHash()
	
	

if __name__ == "__main__":
	main()
