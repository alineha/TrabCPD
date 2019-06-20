#coding=UTF-8
from hashMovie import *
from hashUser import *
from hashGenre import *

def search(hashT, key):

	t = 0
	code = key % hashT.size

	while hashT.table[code] != None:

		if isinstance(hashT, HashMovie):
			ID = hashT.table[code].movieID
		else: 
			ID = hashT.table[code].userID

		if key == ID: 
			return hashT.table[code]
		else: 
			code, t = colision(hashT, code, t)

	return None

def searchStr(hashT, key):

	t = 0
	code = 0

	for ch in key:
		code = (code*33 + ord(ch))
	code = code % hashT.size

	while hashT.table[code] != None:

		if isinstance(hashT, HashGenre):
			selected = hashT.table[code].genre
		#else: 
		#	ID = hashT.table[code].userID

		if key == selected: 
			return hashT.table[code]
		else: 
			code, t = colision(hashT, code, t)

	return None

def colision(hashT, code, t):

	t = t + 1
	code = int(code + 0.5*t + 0.5*t*t) % hashT.size
	return code, t

