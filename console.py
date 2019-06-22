from os import system, name
from searchFunctions import *
import re 

def clrscr(wait=True): 
  
    if wait: input("Pressione ENTER para continuar...\n")

    system('cls' if name == 'nt' else 'clear')

def console(trie, hashMovie, hashUser, hashGenre, hashTag):
    
    word = None

    while word != "quit":

        word = input("Enter the function: ")
        clrscr(False)
        print(word)

        if word[:5] == "movie":

            prefix = word[5:].strip()
            searchTitle(trie, hashMovie, prefix)
            
        elif word[:4] == "user":

            try:
                userID = int(word[4:].strip())
                searchUser(hashUser, hashMovie, userID)
            except:
                print("Incorrect Formating")
                    
        elif word[:3] == "top":

            space = word.find(" ")
            top = word[3:space]
            try:
                top = int(top)
                genre = word[space:].strip()
                print(genre)
                searchGenre(hashGenre, hashMovie, top, genre)
            except:
                print("Incorrect Formating")
            
        elif word[:4] == "tags":

            tags = re.split('\'(.*?)\'', word[4:])
            for tag in tags:
                if tag == "" or tag == " ":
                    tags.remove(tag)
               
            tags = [tag.lower() for tag in tags]
            searchTag(tags, hashTag, hashMovie)

        elif word == "quit":
            print("Program ended gracefully")

        else: 
            print("This command doesn't exist. Type \"quit\" to end execution.")
    
    