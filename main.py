# coding=UTF-8
from trie import Trie

def main():
	trie = Trie()

	trie.insert("Teste número 0", 0)
	trie.insert("Tentativa número 2", 2)
	trie.insert("Traidor número 3", 3)
	trie.insert("Teste dfsfhkj 5", 5)
	
	print(trie.search("Teste nú"))
	
if __name__ == "__main__":
    main()