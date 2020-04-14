from frequencies import NgramFrequencies


def main():

    file_name = input('enter file name: ')

    unigrams = NgramFrequencies(1, file_name)
    bigrams = NgramFrequencies(2, file_name)
    trigrams = NgramFrequencies(3, file_name)

    print("\n Top 10 unigrams:")
    unigrams.make_ngram()
    print("", *unigrams.top_n_freqs(10),
          sep="\n    ")

    print("\n Top 10 bigrams:")
    bigrams.make_ngram()
    print("", *bigrams.top_n_freqs(10),
          sep="\n    ")

    print("\n Top 10 trigrams:")
    trigrams.make_ngram()
    print("", *trigrams.top_n_freqs(10), sep="\n    ")


main()
