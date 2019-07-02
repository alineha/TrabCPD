
# imports for tkinter
import tkinter as tk
from tkinter import ttk
from ttkthemes import *
from tkinter.filedialog import askopenfilename

# imports from other .py files
from searchFunctions import *
from gif import *
from tkAssinc import *

# other imports
import re
import time

global TagName
TagName = "tagOpt.csv"
global MoviesName
MoviesName = "movie.csv"
global ReviewsName
ReviewsName = "ratingOpt.csv"

from hashFunctions import *
from trie import *
import csv

trie = Trie()
hashMovie = HashMovie(size = 45000)
hashUser = HashUser(size = 250000)
hashGenre = HashString(size = 50)
hashTag = HashString(size = 65000)


gltree = False

glscroll = False

glerror = False

def openF(movies, ratings, tags):

	fmovie = open(movies, 'r', encoding="utf8")
	csv_fmovie = csv.reader(fmovie)
	next(csv_fmovie)

	for line in csv_fmovie:

		movieID = int(line[0])
		title = line[1]

		if line[2] != "(no genres listed)":
			genres = line[2].split("|")

			for genre in genres:
				hashGenre.insert(genre, movieID)

		else: genres = None

		trie.insert(title.lower(), movieID)
		hashMovie.insert(movieID, title, genres, None)

	fmovie.close()

	frat =  open(ratings, 'r', encoding="utf8") 
	next(frat)
	for line in frat:
		
		line = line.split(",")
		userID = int(line[0])
		movieID = int(line[1])
		rating = float(line[2])

		hashMovie.insert(movieID, None, None, rating)
		hashUser.insert(userID, movieID, rating)

	frat.close()

	ftag = open(tags, 'r', encoding='utf8')
	csv_ftag = csv.reader(ftag)
	next(csv_ftag)

	for line in csv_ftag:
		movieID = int(line[1])
		tag = (line[2]).lower()
		hashTag.insert(tag, movieID)

	ftag.close()


def main():
	root = ThemedTk(theme = "scidsand")
	root.title("Movie Archive")
	root.iconbitmap("popcorn.ico")
	root.geometry('900x600+300+90')
	frame = ttk.Frame(root)
	frame.place(relheight=1, relwidth=1)

	def askTagFile():
		TagName = askopenfilename()

	def askMoviesFile():
		MoviesName = askopenfilename()

	def askReviewsFile():
		ReviewsName = askopenfilename()

	tagButton = ttk.Button(root, text="Open tags file", command = askTagFile)
	moviesButton = ttk.Button(root, text="Open movies file", command = askMoviesFile)
	reviewsButton = ttk.Button(root, text="Open reviews file", command = askReviewsFile)

	moviesButton.place(x=650, y = 120, height=24, width=200)
	reviewsButton.place(x=650, y = 210, height=24, width=200)
	tagButton.place(x=650, y = 300, height=24, width=200)

	popcornImg = tk.PhotoImage(file = "popcornn.png")
	popcornLabel = tk.Label(frame, image=popcornImg)
	popcornLabel.place(x=60, y=60, height=480, width=480)

	buildButton = ttk.Button(frame, text = "Build archive", command=lambda: opens(frame))
	buildButton.place(x=650, y = 390, height=24, width=200)

	root.mainloop()	

def opens(master):
	def after(self):
		t1 = time.time()
		total = t1-t0
		timetxt = "Finished building data structures. Time: " + str(total)
		timeLabel = ttk.Label(text = timetxt)
		timeLabel.pack()
		gif.destroy()
		loading.destroy()
		searchEntry(master, timeLabel)
	t0 = time.time()
	gif = GifLabel(master)
	gif.place(x=60, y=60, height=480, width=480)
	gif.load('load-min.gif')
	loading = ttk.Label(master, font=("Helvetica Bold", 15), text = "Loading...", compound=tk.CENTER)
	loading.place(x=300, y=520, anchor=tk.N)
	tk_call_async(master, openF, args=(MoviesName, ReviewsName, TagName), callback=after)

def searchEntry(master, timeLabel):
	entry = ttk.Entry(master)
	entry.place(x=650, y = 480, height=24, width=176)
	searchImg = tk.PhotoImage(file = "search2.png")
	searchButton = ttk.Button(master, image=searchImg, compound=tk.CENTER, command = lambda: search(entry.get(), timeLabel, master))
	searchButton.img = searchImg
	searchButton.place(x=826, y=480, height=24, width=24)

def search(word, label, master):

	errorLabel = ttk.Label(text = "Invalid entry.")

	word = word.lower()

	result = None
	label.destroy()
	if word[:5] == "movie":
			prefix = word[5:].strip()
			result = searchTitle(trie, hashMovie, prefix)
			if result is not None:
				printTableMovie(result, master)

	elif word[:4] == "user":

		try:
			userID = int(word[4:].strip())
			result = searchUser(hashUser, hashMovie, userID)
			if result is not None:
				printTableUser(result, master)
		except:
			glerror = errorLabel.pack()
                    
	elif word[:3] == "top":

		space = word.find(" ")
		top = word[3:space]
		try:
			top = int(top)
			genre = word[space:].strip()
			genre = genre[0].upper() + genre[1:].lower()
			result = searchGenre(hashGenre, hashMovie, top, genre)
			if result is not None:
				printTableMovie(result, master)
		except:
			glerror = errorLabel.pack()
            
	elif word[:4] == "tags":

		tags = re.split('\'(.*?)\'', word[4:])
		for tag in tags:
			if tag == "" or tag == " ":
				tags.remove(tag)       
		result = searchTags(tags, hashTag, hashMovie)
		if result is not None:
			printTableMovie(result, master)

	else: 
		glerror = errorLabel.pack()

def printTableUser(table, master):

	global gltree
	global glscroll
	global glerror

	if gltree:
		gltree.destroy()

	if glscroll:
		glscroll.destroy()

	if glerror:
		glerror.destroy()
		glerror = False

	tree = ttk.Treeview(master, columns = (1,2,3), height = 20, show = "headings")
	tree.place(x=175, y=100)

	tree.heading(1, text="ID")
	tree.heading(2, text="Title")
	tree.heading(3, text="Rating")

	tree.column(1, width = 25)
	tree.column(2, width = 250)
	tree.column(3, width = 25)

	scroll = ttk.Scrollbar(master, orient="vertical", command=tree.yview)
	scroll.place(x=475, y=100, height=425)

	tree.configure(yscrollcommand=scroll.set)

	for val in table:
	    tree.insert('', 'end', values = (val[0], val[2].title, val[1]))

	gltree = tree
	glscroll = scroll


def printTableMovie(table, master):

	global gltree
	global glscroll
	global glerror

	if gltree:
		gltree.destroy()

	if glscroll:
		glscroll.destroy()

	if glerror:
		glerror.destroy()

	tree = ttk.Treeview(master, columns = (1,2,3,4), height = 20, show = "headings")
	tree.place(x=50, y=100)

	tree.heading(1, text="ID")
	tree.heading(2, text="Title")
	tree.heading(3, text="Rating")
	tree.heading(4, text="Genres")

	tree.column(1, width = 50)
	tree.column(2, width = 250)
	tree.column(3, width = 50)
	tree.column(4, width = 200)

	scroll = ttk.Scrollbar(master, orient="vertical", command=tree.yview)
	scroll.place(x=600, y=100, height=425)

	tree.configure(yscrollcommand=scroll.set)

	for val in table:
	    tree.insert('', 'end', values = (val.movieID, val.title, val.meanRat, val.genres))

	gltree = tree
	glscroll = scroll

if __name__ == "__main__":
	main()
