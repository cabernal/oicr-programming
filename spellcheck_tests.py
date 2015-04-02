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
    sp = SpellCheck("in_file", "dict_file")
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


def main():
    test_dictionary()
    test_spellcheck()


if __name__ == "__main__":
    main()
