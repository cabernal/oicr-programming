#!/usr/bin/python
from spellcheck import Dictionary, SpellCheck
import sys
#location of dictionary test files
dict_file = "test_files/dict_file"
empty_dict_file = "test_files/dict_file_empty"

#location of input test files
input_file = "test_files/in_file"
bad_punc_input = "test_files/in_file_bad_punctuation"
correct_input = "test_files/in_file_correct"
whitespaces_input = "test_files/in_file_long_whitespaces"
empty_input = "test_files/in_file_empty"
small_input = "test_files/in_file_small"


#redirecting output stream to string list: http://stackoverflow.com/questions/21341096/redirect-print-to-string-list
class ListStream:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def flush(self):
        self.data = []
    def get_data(self):
        return filter(lambda test_stream: test_stream != '\n', self.data)
test_stream = ListStream()

def test_dictionary():
    dictionary = Dictionary(dict_file)
    assert(dictionary.contains("this"))
    assert(dictionary.contains("test"))
    assert(dictionary.contains("document"))
    assert(dictionary.contains("INTERESTING"))
    assert(dictionary.contains("DiFfIcUlt"))
    assert(not dictionary.contains("notcontains"))
    assert(not dictionary.contains("notthis"))
    assert(not dictionary.contains("notindictionary"))
    assert(not dictionary.contains("not document"))
    assert(not dictionary.contains(" this "))
    assert(not dictionary.contains("document "))
    assert(not dictionary.contains("."))
    assert(not dictionary.contains(" "))
    assert(not dictionary.contains(""))
    assert(not dictionary.contains(None))

def test_spellcheck():
    test_errors = ["documnt", "words", "difficlt"]
    in_files = [input_file, whitespaces_input, bad_punc_input]
    sp = SpellCheck("", dict_file)
    for f in in_files:
        sp.set_input_file(f)

        #test SpellCheck#get_misspelling
        assert(sp.get_misspelling("diffut"))
        assert(sp.get_misspelling("Diffut"))
        assert(sp.get_misspelling("DifFut"))
        assert(sp.get_misspelling("documen2") == "documen")
        assert(sp.get_misspelling("thiss?") == "thiss")
        assert(sp.get_misspelling("?thIss") == "thIss")
        assert(sp.get_misspelling("----thiss----") == "thiss")
        assert(sp.get_misspelling("----[thiss2]----") == "thiss")
        assert(not sp.get_misspelling("document"))
        assert(not sp.get_misspelling("document2"))
        assert(not sp.get_misspelling("document-"))
        assert(not sp.get_misspelling("-document"))
        assert(not sp.get_misspelling("-document-"))
        assert(not sp.get_misspelling("[document2]"))
        assert(not sp.get_misspelling(""))
        assert(not sp.get_misspelling(" "))
        assert(not sp.get_misspelling("?"))
        assert(not sp.get_misspelling("2+2=?"))

        #test SpellCheck#get_errors:
        sp.get_errors()
        assert(test_stream.get_data() == test_errors)
        test_stream.flush()

def test_correct_files():
    sp = SpellCheck(correct_input, dict_file)
    sp.get_errors()
    assert(not test_stream.get_data())
    test_stream.flush()

def test_empty_files():
    sp = SpellCheck(empty_input, dict_file)
    sp.get_errors()
    assert(not test_stream.get_data())

    sp = SpellCheck(empty_input, empty_dict_file)
    sp.get_errors()
    assert(not test_stream.get_data())

    test_errors = [ "This", "is", "a", "test", "document"]
    sp = SpellCheck(small_input, empty_dict_file)
    sp.get_errors()
    assert(test_stream.get_data() == test_errors)
    return


def main():
    print("Running tests...")
    sys.stdout = test_stream
    test_dictionary()
    test_spellcheck()
    test_correct_files()
    test_empty_files()
    sys.stdout = sys.__stdout__
    print("All tests passed!")


if __name__ == "__main__":
    main()
