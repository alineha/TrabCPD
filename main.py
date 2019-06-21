# coding=UTF-8
from hash import *
from trie import *
from input import *
import time


def main():

	t0 = time.time()
	trie, hashMovie, hashUser, hashGenre, hashTag = openF()
	t1 = time.time()
	total = t1-t0
	print("\nFinished Loading. Time:",total)
	
	print("\n**********MOVIE**********")
	hashMovie.printHash()
	print("**********USER***********")
	hashUser.printHash()
	print("**********GENRE**********")
	hashGenre.printHash()
	'''
	print("**********TAGS**********")
	hashTag.printHash()
	searchTitle(trie, hashMovie)
	searchUser(hashMovie, hashUser)
	searchGenre(hashGenre)
	searchTags(hashTags)
	'''

if __name__ == "__main__":
	main()
