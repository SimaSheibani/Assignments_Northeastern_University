# This class is the cleaner class! It return clean and edited text.
import re


class TextCleaner:

    def __init__(self, file_name):

        self.file_name = file_name

    def open_file(self):

        try:
            f = open(self.file_name, 'r')
        except FileNotFoundError:
            print('file name is incorrect')
            return
        read_file = f.read().lower()
        new_file_1 = self.change_comma(read_file)
        new_file_2 = self.delet_punctuation(new_file_1)

        new_file_3 = self.split_file(new_file_2)

        return new_file_3

    def split_file(self, file_name):
        # This method delete any period in the midle of sentences! then
        # We can split the sentences with period!

        new_file = file_name.replace('mr.', 'mr').replace('dr.', 'dr\
    ').replace('ms.', 'ms').replace('mrs.', 'mrs')

        file_line = new_file.split('.')

        # delet the last index of file_line list! It was empty!
        file_line = file_line[:-1]

        # with this for loop making another list in file_line.
        # list of words!
        list_word = []
        for word in file_line:
            sub = word.split()
            list_word.append(sub)

        return (list_word)

    def change_comma(self, file_name):
        # this method chang , to COMMA

        return file_name.replace(',', ' COMMA')

    def delet_punctuation(self, file_name):
        # this method get txt and delet all the punctuation in the txt

        punctuation = "!@#$%^&*()_+<>\"?:-;"

        for punc in file_name:
            if punc in punctuation:
                file_name = file_name.replace(punc, '')

        return file_name
