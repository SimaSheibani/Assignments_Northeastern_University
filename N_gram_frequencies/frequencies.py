from text_cleaner import TextCleaner


class NgramFrequencies:

    def __init__(self, N, file_name):

        self.dic_ngram = {}
        self.total_count = 0
        self.N = N

        self.cf = TextCleaner(file_name)

    def make_ngram(self):
        # make n_gram word, convert them to string and add them
        # to dictionary!
        list_ngram = []

        for sentence in self.cf.open_file():
            for i in range((self.N - 1), len(sentence)):
                for j in range(self.N - 1, -1, -1):
                    list_ngram.append(sentence[i - j])
                list_to_str = '_'.join(map(str, list_ngram))
                self.add_item(list_to_str)
                list_ngram = []

    def add_item(self, ngram):
        # This method takes an ngram and increment it's count the dictionary.

        self.total_count += 1

        if ngram in self.dic_ngram.keys():
            self.dic_ngram[ngram] += 1
        else:
            self.dic_ngram[ngram] = 1

    def top_n_counts(self, n):
        # This method return list of words sorted on the count.
        # with the most frequent first.

        sorted_word = sorted(self.dic_ngram.items(),
                             key=lambda x: x[1],
                             reverse=True)
        return sorted_word[:n]

    def frequency(self):
        # This method return dictionary of frequency of words!

        freq_dic = {key: round(self.dic_ngram[key]/self.total_count, 3) for
                    key in self.dic_ngram.keys()}
        return freq_dic

    def top_n_freqs(self, n):
        # This method return list of sorted frequencies of words!

        temp_dic = self.frequency()
        sorted_freq = sorted(temp_dic.items(),
                             key=lambda x: x[1], reverse=True)
        return sorted_freq[:n]
