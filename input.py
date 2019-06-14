from hash import *
from trie import *
import csv

def openF():

	hashT = HashT()
	trie = Trie()

	csv_fmovie = open('movie.csv', 'r', encoding="utf8")
	fmovie = csv.reader(csv_fmovie)
	next(fmovie)
	for line in fmovie:
		movieID = int(line[0])
		title = line[1]
		if line[2] != "(no genres listed)":
			genres = line[2].split("|")
		else:
			genres = []
		trie.insert(title,movieID)
		hashT.insert(title, movieID, genres, None)
	
	frat =  open('minirating.csv', 'r', encoding="utf8") 
	next(frat)

	for line in frat:
		line = line.split(",")
		userID = int(line[0])
		movieID = int(line[1])
		rating = float(line[2])
		hashT.insert(None, movieID, None, rating)

	frat.close()
	csv_fmovie.close()

	hashT.printHashT()
		
	

def main():


	openF()



if __name__ == "__main__":
	main()
