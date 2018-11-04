from __future__ import print_function

import re


class word_with_index(object):
    def __init__(self, word):
        self.word = word
        self.verses_song_1 = []
        self.verses_song_2 = []

    def add_verse_song_1(self, verse):
        self.verses_song_1.append(verse)

    def add_verse_song_2(self, verse):
        self.verses_song_2.append(verse)

    # def assign_verses(self, verses):
    #     self.verses = verses

    def check_verse_song_1(self, verse):
        if verse in self.verses_song_1:
            return True
        else:
            return False

    def check_verse_song_2(self, verse):
        if verse in self.verses_song_2:
            return True
        else:
            return False


def index_finder(file1, file2):
    song1 = open(file1, "r")  # enter your first name
    song2 = open(file2, "r")  # enter your second name
    index = open("index.txt", "w")  # output file

    big_dict = {}
    verse = 1
    for line in song1:
        if line == "" or line == "\n":
            verse += 1
            continue
        line = line.replace("\n", "")
        words = re.split(' |, ', line)
        for word in words:
            temp = big_dict.get(word)
            if temp:
                if not temp.check_verse_song_1(verse):
                    temp.add_verse_song_1(verse)
            else:
                temp_word = word_with_index(word)
                temp_word.add_verse_song_1(verse)
                big_dict[word] = temp_word
    verse = 1
    for line in song2:
        if line == "" or line == "\n":
            verse += 1
            continue
        line = line.replace("\n", "")
        words = re.split(' |, ', line)
        for word in words:
            temp = big_dict.get(word)
            if temp:
                if not temp.check_verse_song_2(verse):
                    temp.add_verse_song_2(verse)
            else:
                temp_word = word_with_index(word)
                temp_word.add_verse_song_2(verse)
                big_dict[word] = temp_word

    it = iter(sorted(big_dict.items()))

    while it:
        try:
            word = it.__next__()
            print("Word: " + word[0] + " ---", " Song 1 Verses: ", big_dict[word[0]].verses_song_1, " Song 2 Verses: ",
                  big_dict[word[0]].verses_song_2 )
            index.write("Word: " + word[0] + " --- Song 1 Verses: ")
            index.writelines(str(big_dict[word[0]].verses_song_1))
            index.write(" Song 2 Verses: ")
            index.writelines(str(big_dict[word[0]].verses_song_2))
            index.write("\n")
        except:

            return


index_finder("song 1.txt", "song 2.txt")
