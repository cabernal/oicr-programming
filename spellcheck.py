#!/usr/bin/python
import sys, re

class Dictionary:
    def __init__(self, dict_file):
        # * use set for fast membership test
        # * set is similar to hash table, it holds a single key instead of a key/value pair
        # * lookup time of set is also O(1)
        self.dict_set= set()
        #load dictonary file into memory
        with open(dict_file) as f:
            for line in f:
                #convert word to lower case and remove trailing new-line characters
                dict_word = line.lower().rstrip()
                self.dict_set.add(dict_word);

    def contains(self, word):
        """
        Return True if word is in the dictionary, false otherwise
        """
        if word:
            #ignore letter case
            return word.lower() in self.dict_set
        return False

class SpellCheck:

    def __init__(self, input_file, dict_file):
        self.input_file = input_file
        self.dictionary = Dictionary(dict_file)

        #compile regex pattern, group 1 contains word to match
        #old regex "[^a-zA-Z]*([a-zA-Z]+)[^a-zA-Z]*$" did not take apostrophes into account
        valid_pattern_str = "[^a-zA-Z]*([a-zA-Z]+(\'[a-zA-Z])?)[^a-zA-Z]*$"
        self.valid_pattern = re.compile(valid_pattern_str)

    def set_input_file(self, input_file):
        self.input_file = input_file

    def get_misspelling(self, token):
        """
        If there is a spelling error in the token, return the matched error 
        otherwise return None
        """
        token_match = self.valid_pattern.match(token)
        if token_match:
            word_match = token_match.group(1)
            if not self.dictionary.contains(word_match):
                return word_match
        return None

    def get_errors(self):
        """
        Return a list containing all spelling errors of input file wrt dictionary.
        """
        misspellings = []
        with open(self.input_file) as f:
            #loop through file, in case there is more than one line
            for line in f:
                #split on whitespaces and print any words not found in dictionary
                for token in line.split():
                    spelling_error = self.get_misspelling(token)
                    if spelling_error: print(spelling_error)


def usage():
    print("usage: python spellcheck.py input_file dictionary_file")

def main(argv):
    #make sure we have input and dictionary files
    if len(argv) != 2:
        usage()
        sys.exit()

    #create SpellCheck object with given input and dictionary files and print any errors
    sp = SpellCheck(argv[0], argv[1])
    sp.get_errors()

if __name__ == "__main__":
    main(sys.argv[1:])


    
