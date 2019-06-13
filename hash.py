#coding=UTF-8

#Nodo da estrutura hash
class nodeHashT:

    def __init__(self, title, movieID, genres, meanRat, count = 0):

        self.title = title

        self.movieID = movieID
    
        self.genres = genres
        
        self.meanRat = meanRat
        
        self.count = count

    def __str__(self):
        return "TITLE: {} | MOVIE ID: {} | MEAN RATING: {} | COUNT: {}".format(self.title, self.movieID, self.meanRat, self.count) + " | GENRES: " +  str(self.genres)

class HashT:

    def __init__(self, size = 8):

        self.size = size

        self.table = [None]*size

        self.taken = 0

        self.rate = (self.taken / self.size)*100
        

    def insert(self, movieID, title, genres, rating, count = 1):
        
        t = 0
        code = self.horner(movieID)
        while self.full(code):
            if movieID == self.table[code].movieID:
                self = self.nodeUpdt(code, rating)
                return self
            else:
                code = self.colision(code, t)

        node = nodeHashT(title, movieID, genres, rating, count)
        self.table[code] = node
        self = self.incTaken()
        self = self.reSize()
        del node
        return self


    def horner(self, code):

        strcode = str(code)
        result = 0 
   
        for i in range(0, len(strcode)): 
            result = (result*33 + int(strcode[i]))
        result = result % self.size 
       
        return result 

    def full(self, code):

        return False if self.table[code] == None else True
            

    def colision(self, code, t):

        c = 0.5
        t = t + 1
        code = int(code + c*t + c*t*t) % self.size
        return code


    def nodeUpdt(self, code, rating):
    
        #self.table[code].genres = genres
        
        self.table[code].meanRat = (rating + self.table[code].meanRat)/2
        
        self.table[code].count = self.table[code].count + 1

        return self


    def reSize(self):

        if self.rate >= 67:
            listAux = [None]*self.size 
            self.table.extend(listAux) 
            del listAux
            self.size = len(self.table)
            self.rate = (self.taken/self.size)*100

        self.printHashT()

        return self


    def incTaken(self):
        self.taken = self.taken + 1
        self.rate = (self.taken / self.size)*100

        return self


    def printHashT(self):
        print(self)
        for nodo in self.table:
            print(str(nodo))


    def __str__(self):
        return " * SIZE: {} | TAKEN: {} | RATE: {}".format(self.size, self.taken, self.rate)
