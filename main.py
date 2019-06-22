# coding=UTF-8
from input import *
from console import *
import time

def main():

	t0 = time.time()

	trie, hashMovie, hashUser, hashGenre, hashTag = openF()

	t1 = time.time()
	total = t1-t0
	print("\nFinished Loading. Time:",total)

	console(trie, hashMovie, hashUser, hashGenre, hashTag)
	

if __name__ == "__main__":
	main()
