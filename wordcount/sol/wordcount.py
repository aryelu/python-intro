#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

BOOK_FILENAME = 'book1_01'

def read_file(filename):
    with open(filename) as fd:
        lines = fd.readlines()
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]
    return lines


def line_to_words(line):
    return line.split(" ")


def load_words(filename):
    words_dict = {}
    lines = read_file(filename)
    word_lists = [line_to_words(line) for line in lines]
    for word_list in word_lists:
        words = [word.lower() for word in word_list]
        for word in words:
            words_dict[word] = words_dict.setdefault(word, 0) + 1
    return words_dict

def print_word_count(word, count):
    print "%s\t%d" % (word, count)

def print_words(filename):
    words = load_words(filename)
    for word, count in words.iteritems():
        print_word_count(word, count)


def print_top(filename):
    words = load_words(filename)
    word_list = [(word, count) for word, count in  words.iteritems()]
    word_list.sort(key=lambda (word, count): count, reverse=True)
    for word, count in word_list[:20]:
        print_word_count(word, count)


def print_count():
    print_words(BOOK_FILENAME)

def print_topcount():
    print_top(BOOK_FILENAME)