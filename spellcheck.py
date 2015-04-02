#!/usr/bin/python
import sys, re

class Dictionary:
    def __init__(self, dict_file):
        self.dict_list = []
        #load dictonary file into memory
        with open(dict_file) as f:
            for line in f:
                #convert word to lower case before appending to list
                #TODO: Remove trailing/leading non-alphabetic chars
                self.dict_list.append(line.lower().rstrip())

    def contains(self, word):
        #TODO: Check empty/null args, try binary search
        if word:
            input_word = word.lower()
            for dict_word in self.dict_list:
                if input_word in self.dict_list:
                    return True
        return False


class SpellCheck:

    def __init__(self, input_file, dict_file):
        self.input_file = input_file
        self.dictionary = Dictionary(dict_file)

        #compile regex pattern
        valid_pattern_str = "[^a-zA-Z]*([A-zA-Z]+)[^a-zA-Z]*$"
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
        Return a list containing all spelling errors.
        """
        misspellings = []
        with open(self.input_file) as f:
            #loop through file, in case there is more than one line
            for line in f:
                for token in line.split():
                    spelling_error = self.get_misspelling(token)
                    if spelling_error: misspellings.append(spelling_error)
        return misspellings


def usage():
    print "usage: python spellcheck.py input_file dictionary_file"

def print_list(l):
    for i in l:
        print i

def main(argv):
    #make sure we have input and dictionary files
    if len(argv) != 2:
        usage()
        sys.exit()

    #create SpellCheck object with given input and dictionary files and print any errors
    sp = SpellCheck(argv[0], argv[1])
    print_list(sp.get_errors())

if __name__ == "__main__":
    main(sys.argv[1:])


    
