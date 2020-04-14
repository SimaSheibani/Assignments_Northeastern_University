from frequencies import NgramFrequencies


def test_constructor():
    '''Test the constructor'''
    ngram_freq = NgramFrequencies(2, '')
    assert ngram_freq.dic_ngram == {}
    assert ngram_freq.total_count == 0
    assert ngram_freq.N == 2


def test_make_ngram():
    '''Test the make ngram method'''
    ngram_freq = NgramFrequencies(1, 'test_file.txt')
    ngram_freq_2 = NgramFrequencies(2, 'test_file.txt')
    ngram_freq.make_ngram()
    ngram_freq_2.make_ngram()
    assert list(ngram_freq.dic_ngram.keys()) == ['ab', "dr", 'd', 'gh', 'COMMA', "ab's"]
    assert list(ngram_freq_2.dic_ngram.keys()) == ['ab_dr', "dr_d", 'gh_COMMA', "COMMA_ab's"]


def test_add_item():
    '''Test the add item method'''
    ngram_freq = NgramFrequencies(1, '')
    ngram_freq.add_item('ab')
    assert ngram_freq.dic_ngram['ab'] == 1


def test_top_n_counts():
    '''Test the top n counts method'''
    ngram_freq = NgramFrequencies(1, '')
    ngram_freq.dic_ngram["ab"] = 3
    ngram_freq.dic_ngram["cd"] = 2
    ngram_freq.dic_ngram["ef"] = 6
    list_top_count = ngram_freq.top_n_counts(3)
    assert list_top_count[0][0] == "ef"
    assert list_top_count[1][0] == "ab"
    assert list_top_count[2][0] == "cd"


def test_frequency():
    '''Test the frequency method'''
    ngram_freq = NgramFrequencies(1, '')
    ngram_freq.dic_ngram["a"] = 3
    ngram_freq.dic_ngram["c"] = 2
    ngram_freq.dic_ngram["e"] = 6
    ngram_freq.total_count = 11
    new_dic = ngram_freq.frequency()
    assert new_dic["a"] == round(3/11, 3)


def test_top_n_freqs():
    '''Test the top n reqs method'''
    ngram_freq = NgramFrequencies(1, '')
    ngram_freq.dic_ngram["ab"] = 1
    ngram_freq.dic_ngram["cd"] = 7
    ngram_freq.dic_ngram["ef"] = 12
    ngram_freq.total_count = 20
    list_top_freq = ngram_freq.top_n_freqs(3)
    assert list_top_freq[0][0] == "ef"
    assert list_top_freq[1][0] == "cd"
    assert list_top_freq[2][0] == "ab"
