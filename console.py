from os import system, name
from searchFunctions import *
import re

def clrscr(wait = True): 
  
    if wait: input("Pressione ENTER para continuar...\n")

    system('cls' if name == 'nt' else 'clear')

def console(trie, hashMovie, hashUser, hashGenre, hashTag):
    
    word = None

    while word != "quit":

        word = input("\nEnter the function: ")
        clrscr(False)

        if word[:5] == "movie":

            prefix = word[5:].strip()
            searchTitle(trie, hashMovie, prefix.lower())
            
        elif word[:4] == "user":

            try:
                userID = int(word[4:].strip())
                searchUser(hashUser, hashMovie, userID)
            except:
                print("Something is wrong")
                    
        elif word[:3] == "top":

            space = word.find(" ")
            top = word[3:space]
            try:
                top = int(top)
                genre = word[space:].strip()
                searchGenre(hashGenre, hashMovie, top, genre)
            except:
                print("Something is wrong")
            
        elif word[:4] == "tags":

            tags = re.split('\'(.*?)\'', word[4:])
            for tag in tags:
                if tag == "" or tag == " ":
                    tags.remove(tag)
               
            tags = [tag.lower() for tag in tags]
            searchTags(tags, hashTag, hashMovie)

        elif word == "quit":
            print("Program ended gracefully")

        else: 
            print("Invalid function. Type \"quit\" to exit program.")
    
    