"""Word Finder: finds random words from a dictionary."""
from random import randint, choice
import random
class WordFinder:
    """   
    ## **Random Word**
    Takes a file, a newline delimeted word list and returns the total number of words
    in the list. It also provides a mehtod for returning a random word in the list.
    """

    def __init__(self, path):
        """open and read 'path' into a string word_list close file and call count"""

        self.path = path
        self.file = open(self.path, 'r')
        word_list = self.file.read()
        self.lst = word_list.splitlines()
        self.file.close()
        self.line_count()

    def line_count(self):
        """use lenght ot the array for the number of words"""
        print(f"There are {len(self.lst)} words in the file {self.path}")


    def random(self):
        """create a list out of everyword in the file and return a random indexed word"""
        line_num = randint(0, len(self.lst) -1)
        print(f"the {line_num + 1}th word is ",self.lst[line_num])
        

class SpecialWordFinder(WordFinder):
    """ extends class WordFinder uses methods count and random from super()"""

    def __init__(self, path):
        """filters word list to only contain words.no comments or blank lines, would have liked to do this with regex at the string level"""
        self.path = path
        self.lst = []
        file = open(path,'r')
        word_list  = file.read()
        file.close()

        tmp_lst = word_list.splitlines()
        for line in tmp_lst:
            if line and not line.startswith('#') and not line.isspace():
                self.lst.append(line)
        
        self.line_count()

        
        
# x = SpecialWordFinder('words.txt')
# x.random()
    
