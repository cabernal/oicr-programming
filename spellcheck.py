import sys, re

"""
Notes
    * Can ignore case
    * Should we convert to small case as we load in files?
    * Convert to lower case on find calls
    * Frequency of misspelling should be less than number of words
"""

class Dictionary:
    def __init__(self, dict_file):
        self.dict_list = []
        #load dictonary file into memory
        with open(dict_file) as f:
            for line in f:
                #convert word to lower case before appending to list
                #TODO: Remove trailing/leading non-alphabetic chars
                self.dict_list.append(line.lower().rstrip('\n'))

    def contains(self, word):
        #TODO: Check empty/null args, try binary search
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

    def is_misspelled(self, token):
        token_match = self.valid_pattern.match(token)
        if token_match:
            word_match = token_match.group(1)
            return not self.dictionary.contains(word_match)
        return False

    def get_errors2(self):
        misspellings = []
        with open(self.input_file) as f:
            for line in f:
                print line.split
                cur_errors = filter(self.is_misspelled, line.split())
                misspellings.extend(cur_errors)
        return misspellings
        
        

    def get_errors(self):
        misspellings = []
        with open(self.input_file) as f:
            #TODO: Could replace with readLine()
            #      Could try a map
            for line in f:
                for token in line.split():
                    #match token
                    token_match = self.valid_pattern.match(token)
                    if token_match:
                        word_match = token_match.group(1)
                        if not self.dictionary.contains(word_match):
                            misspellings.append(word_match)
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

    sp = SpellCheck(argv[0], argv[1])
    print_list(sp.get_errors2())

if __name__ == "__main__":
    main(sys.argv[1:])


    
