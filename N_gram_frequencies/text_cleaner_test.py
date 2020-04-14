from text_cleaner import TextCleaner


def test_constructor():
    '''Test the constructor'''
    clean_file = TextCleaner('test')
    assert clean_file.file_name == 'test'


def test_open_file():
    '''Test the open file method'''
    clean_file = TextCleaner('test_file.txt')
    actual_list = clean_file.open_file()
    assert actual_list == [["ab", "dr", "d"], ["gh", "COMMA", "ab's"]]


def test_split_file():
    '''Test the split file method'''
    clean_file = TextCleaner("")
    actual_list = clean_file.split_file("mr. dr. ms. ab cd. ab ab.")
    assert actual_list == [['mr', 'dr', 'ms', 'ab', 'cd'], ['ab', 'ab']]


def test_change_comma():
    '''Test the change comma method'''
    clean_file = TextCleaner("")
    actual_string = clean_file.change_comma("ab, cd,")
    assert actual_string == "ab COMMA cd COMMA"


def test_delete_punctuation():
    '''Test the delete punctuation method'''
    clean_file = TextCleaner("")
    actual_string = clean_file.delet_punctuation("ab)($><")
    assert actual_string == "ab"
