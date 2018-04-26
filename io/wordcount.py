#!/usr/bin/env python3
# A Simple python program to count the number of times a word has occured in a file
import sys


def word_count(filename):
    results = dict()
    with open(filename,"r") as f:
        for line in f:
            for word in line.split():
                results[word] = results.setdefault(word,0) + 1

    for word, count in sorted(results.items(), key=lambda x : x[1]):
        print("{} - {}".format(word,count))


if __name__ == '__main__':
    filename = sys.argv[1]
    word_count(filename)



