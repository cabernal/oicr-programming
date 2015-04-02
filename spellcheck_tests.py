#!/usr/bin/python
from spellcheck import Dictionary, SpellCheck

def test_dictionary():
    dictionary = Dictionary("dict_file")
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
    in_files = ["in_file",
                "in_file_long_whitespaces",
                "in_file_bad_punctuation"]
    sp = SpellCheck("", "dict_file")
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
        assert(sp.get_errors() == test_errors)

def test_correct_files():
    sp = SpellCheck("in_file_correct", "dict_file")
    assert(not sp.get_errors())

def test_empty_files():
    sp = SpellCheck("in_file_empty", "dict_file")
    assert(not sp.get_errors())

    test_errors = [ "This", "is", "a", "test", "document"]

    sp = SpellCheck("in_file_small", "dict_file_empty")
    assert(sp.get_errors() == test_errors)
    return


def main():
    test_dictionary()
    test_spellcheck()
    test_correct_files()
    test_empty_files()


if __name__ == "__main__":
    main()
