# Python script to check the number of files, find duplicates, sizes of the files
import os
import sys


def filecount(dir_location):
    files = os.listdir(dir_location)
    sym_links_files = []
    regular_files = []
    for file in files:
        name = os.path.abspath(os.path.join(dir_location,file))
        if os.path.islink(name):
            sym_links_files.append(name)
        else :
            regular_files.append(name)
    display(sym_links_files,"symlinks")
    display(regular_files,"regular")


def decorate(fun):
    def decorate_display(files, filetype):
        print("-------------------")
        print(filetype)
        fun(files,filetype)
        print("-------------------")
    return decorate_display


@decorate
def display(files,filetype):
    for count, file in enumerate(files):
        print("{0} - {1} - {2}".format(count,filetype,file))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough number of args to filechecker")
        print("Usage: filechecker.py <directory_name>")
        sys.exit(1)

    location = sys.argv[1]

    if os.path.isdir(location):
        print(location + " is a directory and exists")
        filecount(location)
    else:
        print("Input argument is invalid. Target Directory location is not directory")
        sys.exit(1)
