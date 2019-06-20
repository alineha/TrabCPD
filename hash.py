#coding=UTF-8
from hashMovie import *
from hashUser import *
from hashGenre import *


def search(hashT, ID):

	t = 0
	code = ID % hashT.size

	while hashT.table[code] != None:

		if isinstance(hashT, HashMovie):
			key = hashT.table[code].movieID

		else: key = hashT.table[code].userID

		if ID == key: return hashT.table[code]
		else: code, t = colision(hashT, code, t)

	return None

def searchStr(hashT, string):

	t = 0
	code = 0

	for ch in string:
		code = (code*33 + ord(ch)) % hashT.size

	while hashT.table[code] != None:

		if isinstance(hashT, HashGenre):
			key = hashT.table[code].genre
		#else: 
		#	key = hashT.table[code].tag

		if string == key: return hashT.table[code]
		else: code, t = colision(hashT, code, t)

	return None

def colision(hashT, code, t):

	t = t + 1
	code = int(code + 0.5*t + 0.5*t*t) % hashT.size
	return code, t

