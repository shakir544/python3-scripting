# Python example of read and write
import sys
# open a text file


def readfile(filename):
    with open(filename,"rt") as file :
        for line in file :
            print(line)


if __name__ == '__main__':
    filename = sys.argv[1]
    readfile(filename)